#First API Call wrt  Gemini
import google.generativeai as genai
import os 
from dotenv import load_dotenv

#load the apikey from the dotenv file we created yesterday
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#Create a modle instance with config
model = genai.GenerativeModel(model="gemini-2.5-flash",
                              generation_config={"temperature":0.7,
                                                 "max_output_tokens":150},
                                                 system_instruction="You are a concise AI tutor. Answer in 2-3 sentences")

#Call the model 
result = model.generate_content("What is a Vector database ?")
print(result.text)
print(f"Tokens: {result.usage_metadata.total_token_count}")