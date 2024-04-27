from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import base64
import requests

load_dotenv()

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
        for jpg in jpg_data['Files']:
            body = {
                "url" : jpg["Url"],
                "apikey": api_key
            }
            ocr_text = requests.post(ocr_url, data=body)
            ocr_response = ocr_text.json()
            for ocr in ocr_response['ParsedResults']:
                result += ocr['ParsedText']
                result += "\n\n-next page-\n\n"
        return result

    return "Wrong file format", 415


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)