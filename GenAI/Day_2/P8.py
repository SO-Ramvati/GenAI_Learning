# Zero-shot prompting using Gemini
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load the API key from your local .env file
load_dotenv()

# Initialize the client using the new google-genai SDK syntax
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """Classify the sentiment of this review as Positive, Negative, or Neutral.
Reply with one word only.

Review: "Lengthy classes
Teachers are good but manager 's behaviour is not good
Ek hi batch par focus Krna jiske kaaran dusra batch damaged
Time par course khtm nhi hota baki content acha h" """

def ask(prompt):
    # Call the model via the client object using the new syntax
    result = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=150,
        )
    )
    return result.text.strip()

# Execute the function with the target prompt
print(ask("Classify: 'Great product!' — Positive, Negative, or Neutral. One word."))