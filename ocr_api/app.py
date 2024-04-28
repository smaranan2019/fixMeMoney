from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./firebase/gemini-fixmemoney-firebase-adminsdk-s5ncw-bc46093f91.json")
db_app = firebase_admin.initialize_app(cred)
db = firestore.client()

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)
CORS(app)
port = 5200

api_key=os.getenv("API_KEY")
headerInfo = {
    'apikey': api_key
}
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

@app.route("/ocr", methods=['POST'])
def convertImageToText():
    if 'file' not in request.files:
        return "no file provided", 400

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return "no file provided", 400

    if file and allowed_file(file.filename): # allow only pdf

        # Start of converting PDF to JPG
        files={'file':(file.filename, file.stream, file.content_type, file.headers)}
        jpg_response = requests.post(pdf_2_jpg_url, files=files)
        jpg_data = jpg_response.json()
        # End of converting PDF to JPG
        result = ""
        gemini_response_text = ""
        for jpg in jpg_data['Files']:
            body = {
                "url" : jpg["Url"],
                "apikey": api_key
            }
            ocr_text = requests.post(ocr_url, data=body)
            ocr_response = ocr_text.json()
            for ocr in ocr_response['ParsedResults']:
                result += ocr['ParsedText'] # str
                result += "\n\n-next page-\n\n"
                # for each page, using Gemini, convert OCR text to table data
                gemini_response = model.generate_content(gemini_prompt + "\n\n" + result)
                gemini_response_text += gemini_response.text + "\n\n-next page-\n\n"
                # process table data and save to temp_db
        return gemini_response_text

    return "Wrong file format", 415

# convert OCR text to table using Gemini
# for each row, generate category using Gemini
# save into temp_db pending user edits and confirmation
# when save and fetch data, got userid

@app.route("/transactions", methods=['GET'])
def getTransactions():
    transactions = []
    transactions_ref = db.collection("transactions").stream()

    for transaction in transactions_ref:
        if transaction.exists:
            transaction_data = transaction.to_dict()
            transaction_data['id'] = transaction.id  # Include the document ID in the data
            transactions.append(transaction_data)
    return transactions

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)