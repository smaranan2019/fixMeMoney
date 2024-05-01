import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)


model_vision = genai.GenerativeModel('gemini-pro-vision')
image = PIL.Image.open('test.jpg')
gemini_prompt = "Convert the image of bank statement into table data. Include only Trans Date, Description of Transaction and Transaction Amount as columns. 'PREVIOUS BALANCE' does not have Post Date and Trans Date.\n"
response = model_vision.generate_content(
    [gemini_prompt, image],
)
response.resolve()
print(response.text)
