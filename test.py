import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAkOcFbE01fv_5nEU_YDjReVz8TfMXHN2w')

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Say hi')

print(response.text)