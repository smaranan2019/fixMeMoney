import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)