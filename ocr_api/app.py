from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import base64
import requests

load_dotenv()

app = Flask(__name__)
port = 5200

api_key=os.getenv("API_KEY")

ocr_url = 'https://api.ocr.space/parse/image'

@app.route("/ocr", methods=['POST'])
def convertImageToText():
    if 'file' not in request.files:
        return "no file provided"

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return "no file provided"

    if file:
        headerInfo = {
            'apikey': api_key
        }

        files={'file':(file.filename, file.stream, file.content_type, file.headers)}

        # print(api_body)
        ocr_text = requests.post(ocr_url, files=files, headers=headerInfo)
        ocr_response = ocr_text.json()

        if len(ocr_response['ParsedResults']) > 0:
            return ocr_response['ParsedResults'][0]['ParsedText']

    return "No ocr data returned"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)