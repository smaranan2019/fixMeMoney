from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai
from constants import gemini_prompt, ocr_url
from db import Database
from user import User
from bank import BankStatementProcessor
from firebase_admin import credentials

cred = credentials.Certificate("./firebase/gemini-fixmemoney-firebase-adminsdk-s5ncw-bc46093f91.json")
db = Database(cred)

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

bankStatementProcessor = BankStatementProcessor()

app = Flask(__name__)
CORS(app)
port = 5200

ocr_api_key=os.getenv("OCR_API_KEY")

pdf_api_key=os.getenv("PDF_API_KEY")
pdf_2_jpg_url = 'https://v2.convertapi.com/convert/pdf/to/jpg?Secret=' + pdf_api_key + '&StoreFile=true'


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
                result = ocr['ParsedText'] # str
                result += "\n\n-next page-\n\n"
                # For each image (page), convert OCR text to table data and generate categories using Gemini
                gemini_response = model.generate_content(gemini_prompt + "\n\n" + result)
                gemini_response_text += gemini_response.text + "\n\n-next page-\n\n"

        print("\nGemini table data:\n", gemini_response_text)
        
        # Get userId
        userId = User.getUserId()

        # Convert Gemini table text to list of transactions for user
        transactions_list = bankStatementProcessor.convertGeminiTableToList(gemini_response_text, userId)
        
        # Save transactions to database for user
        db.saveToDb(transactions_list)
        
        return transactions_list, 200

    return "Wrong file format", 415

@app.route("/transactions", methods=['GET'])
def getTransactionsForUser():
    # Get userId from request args
    userId = request.args.get('userId')
    if not userId or not userId.isnumeric():
        # Return an error response if userId is None / empty / non-numeric
        return "UserId is missing / not a number", 400
    # Create a query against the collection
    transactions = db.queryTransactionsForUserToConfirm(int(userId))
    return transactions, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)