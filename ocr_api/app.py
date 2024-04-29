from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import uuid
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("./firebase/gemini-fixmemoney-firebase-adminsdk-s5ncw-bc46093f91.json")
db_app = firebase_admin.initialize_app(cred)
db = firestore.client()

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)
CORS(app)
port = 5200

ocr_api_key=os.getenv("OCR_API_KEY")
ocr_url = 'https://api.ocr.space/parse/image'

pdf_api_key=os.getenv("PDF_API_KEY")
pdf_2_jpg_url = 'https://v2.convertapi.com/convert/pdf/to/jpg?Secret=' + pdf_api_key + '&StoreFile=true'

gemini_prompt =  """Given:
- The columns are 'Trans' (date), 'Description of Transaction' (string), 'Transaction Amount' (decimal).
- Exclude 'Post' column and its values.
- Ignore 'Ref No.' only.
Convert the following text into table data:"""

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/submitPdf", methods=['POST'])
def convertPdfToData():
    if 'file' not in request.files:
        return "No file provided", 400

    file = request.files['file']

    if file.filename == '':
        return "No file provided", 400

    if file and allowed_file(file.filename): # Allow only pdf
        # Start of converting PDF to JPG
        files={'file':(file.filename, file.stream, file.content_type, file.headers)}
        jpg_response = requests.post(pdf_2_jpg_url, files=files)
        jpg_data = jpg_response.json()
        # End of converting PDF to JPG
        result = ""
        gemini_response_text = ""
        # Start of converting JPG to text
        for jpg in jpg_data['Files']:
            body = {
                "url" : jpg["Url"],
                "apikey": ocr_api_key
            }
            ocr_text = requests.post(ocr_url, data=body)
            ocr_response = ocr_text.json()
            # End of converting JPG to text
            for ocr in ocr_response['ParsedResults']:
                result += ocr['ParsedText'] # str
                result += "\n\n-next page-\n\n"
                # For each image (page), convert OCR text to table data using Gemini
                gemini_response = model.generate_content(gemini_prompt + "\n\n" + result)
                gemini_response_text += gemini_response.text + "\n\n-next page-\n\n"
                # Process table data and save to temp_db
        print("Gemini table data:\n", gemini_response_text)
        # Get userId
        userId = getUserId()
        # Convert Gemini table text to list of transactions for user
        transactions_list = convertGeminiTableToList(gemini_response_text, userId)
        # Save transactions to database for user
        saveToDb(transactions_list)
        
        return convertGeminiTableToList(gemini_response_text, userId), 200

    return "Wrong file format", 415

def getUserId():
    # Assumption: 1 user for demo
    return 1

def convertGeminiTableToList(gemini_response_text, userId):
    lines = gemini_response_text.strip().split('\n')
    # Remove the header and the separator lines
    lines = lines[2:]
    # Initialize list of dict to store transactions
    transactions = []
    for line in lines:
        # Detect end of transactions
        if line == '' or '-next page-' in line:
            break
        # Strip the leading and trailing '|' and split by '|'
        parts = [part.strip() for part in line.split('|')]
        # Extract the fields
        trans_date = parts[1]
        desc = parts[2]
        amount_str = parts[3].replace(',', '').replace('SGD', '').strip() # Remove 'SGD' and ','
        print(trans_date, desc, amount_str)
        type_str = 'debit' # Set 'type' as debit by default
        # Check if the amount is a credit and handle it
        if 'CR' in amount_str:
            # Remove 'CR', strip any whitespace, and convert to float
            amount = float(amount_str.replace('CR', '').strip())
            # Set 'type' as credit
            type_str = 'credit'
        else:
            # Strip any whitespace, and convert to float
            amount = float(amount_str.strip())
        
        # Create a dictionary for the transaction
        transaction = {
            'transDate': trans_date,
            'desc': desc,
            'amount': amount,
            'type': type_str,
            'userId': userId,
            'category': getCategory()
        }
        # Add the dictionary to the list
        transactions.append(transaction)
    # Check for 'PREVIOUS BALANCE'
    transactions = checkForPreviousBalance(transactions)

    return transactions

def getCategory():
    # TODO: for each row, generate category using Gemini
    return 'category to be generated by Gemini'

def checkForPreviousBalance(transactions):
    # Variable to keep track of the last valid transaction date
    last_valid_date = None
    # Check if the first transaction has 'PREVIOUS BALANCE' and handle it
    if 'PREVIOUS BALANCE' in transactions[0]['desc']:
        last_valid_date = transactions[0]['transDate']
        # Remove "PREVIOUS BALANCE"
        transactions.pop(0)
        # Iterate through the modified list
        for transaction in transactions:
            if last_valid_date is not None:
                current_valid_date = transaction['transDate']
                # Update transDate to previous transDate, last_valid_date
                transaction['transDate'] = last_valid_date
            last_valid_date = current_valid_date
    return transactions

def saveToDb(transactions_list):
    # Add a new doc (transaction) in collection 'transactions'
    # Each doc's id is randomly generated uuid
    for transaction in transactions_list:
        db.collection("transactions").document(str(uuid.uuid4())).set(transaction)





# convert OCR text to table using Gemini
# TODO 1: for each transaction, change transDate from string to datetime
# TODO 2: for each transaction, generate category using Gemini
# save into db pending user edits and confirmation
# when save and fetch data, got userid

@app.route("/transactions", methods=['GET'])
def getTransactionsForUser():
    # Get userId from request args
    userId = request.args.get('userId')
    if not userId:
        # Return an error response if userId is None or empty
        return "UserId is missing", 400
    # Create a reference to the transactions collection
    transactions_ref = db.collection("transactions")

    # Create a query against the collection
    user_transactions_ref = transactions_ref.where(filter=FieldFilter("userId", "==", int(userId))).stream()
    transactions = []
    for transaction in user_transactions_ref:
        if transaction.exists:
            transaction_data = transaction.to_dict()
            transaction_data['id'] = transaction.id  # Include the document ID in the data
            transactions.append(transaction_data)
    return transactions, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)