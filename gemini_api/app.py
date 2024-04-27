from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
port = 5100

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gemini")
def generateText():
    response = "Not available";
    data = request.json
    if (data["text"]) :
        response = model.generate_content(data["text"])

    print(response)
    return jsonify({
        "response" : response.text
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)