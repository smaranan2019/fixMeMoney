from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai
from constants import gemini_prompt, ocr_url, allowed_file, result_page_1
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
headerInfo = {
    'apikey': ocr_api_key
}

pdf_api_key=os.getenv("PDF_API_KEY")
pdf_2_jpg_url = 'https://v2.convertapi.com/convert/pdf/to/jpg?Secret=' + pdf_api_key + '&StoreFile=true'


@app.route("/submitPdf", methods=['POST'])
def convertPdfToData():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file provided"}), 400
    if file and allowed_file(file.filename): # Allow only pdf
        # Start of converting PDF to JPG
        print("\nStart of converting PDF to JPG using OCR")
        files={'file':(file.filename, file.stream, file.content_type, file.headers)}
        jpg_response = requests.post(pdf_2_jpg_url, files=files)
        jpg_data = jpg_response.json()
        print("\nOCR jpg response:\n", jpg_data)
        # End of converting PDF to JPG
        result = ""
        gemini_response_text = ""
        print("\nEnd of converting JPG to text using OCR")
        # Start of converting JPG to text
        print("\nStart of converting JPG to text using OCR")
        for jpg in jpg_data['Files']:
            body = {
                "url" : jpg["Url"],
                "apikey": ocr_api_key
            }
            ocr_text = requests.post(ocr_url, data=body, headers=headerInfo)
            ocr_response = ocr_text.json()
            # Check if OCR API is down
            if ocr_response['IsErroredOnProcessing']:
                url = jpg["Url"]
                return jsonify({"error": f"OCR API to convert JPG to text failed for {url}"}), 404
            # End of converting JPG to text
            for ocr in ocr_response['ParsedResults']:
                result = ocr['ParsedText'] # str
                result += "\n\n-next page-\n\n"
                # For each image (page), convert OCR text to table data and generate categories using Gemini
                gemini_response = model.generate_content(gemini_prompt + "\n\n" + result)
                gemini_response_text += gemini_response.text + "\n\n-next page-\n\n"
        print("\nGemini table data with categories:\n", gemini_response_text)
        # Get userId
        userId = User.getUserId()
        # Convert Gemini table text to list of transactions for user
        transactions_list = bankStatementProcessor.convertGeminiTableToList(gemini_response_text, userId)
        # Save transactions to database for user
        db.saveToDb(transactions_list)
        return jsonify(transactions_list), 200
    return jsonify({"error": "Wrong file format"}), 415

@app.route("/transactions", methods=['GET'])
def getTransactionsForUser():
    # Get userId from request args
    userId = request.args.get('userId')
    if not userId or not userId.isnumeric():
        # Return an error response if userId is None / empty / non-numeric
        return jsonify({"error": "UserId is missing / not a number"}), 400
    # Create a query against the collection
    transactions = db.queryTransactionsForUserToConfirm(int(userId))
    return jsonify(transactions), 200

@app.route("/transactionsConfirm", methods=['POST'])
def confirmTransactionsForUser():
    # Get transactions from body of request
    transactions = request.get_json(silent=True)
    if not transactions:
        return jsonify({"error": "No transactions provided"}), 400
    # Check on transactions
    for transaction in transactions:
        if not bankStatementProcessor.isValidTransaction(transaction):
            return jsonify({"error": "Invalid transactions provided"}), 415
    # Filter transactions where 'userConfirm' = True
    confirmed_transactions = [transaction for transaction in transactions if transaction.get('userConfirm', True)]
    if confirmed_transactions:
        db.confirmTransactionsForUser(confirmed_transactions, True)
    # Update all transactions to userConfirm=True
    db.confirmTransactionsForUser(transactions, False)
    return jsonify({"message": "Transactions saved successfully"}), 200

@app.route("/transactionsUnconfirm", methods=['GET']) # For testing
def unconfirmTransactionsForUser():
    # Update all transactions to userConfirm=False (unconfirm)
    db.unconfirmTransactionsForUser()
    return jsonify({"message": "Transactions unconfirmed successfully"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)