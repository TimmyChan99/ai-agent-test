import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        print("Add a prompt as an argument to the script.")
        sys.exit(1)
    
    verbose_flag = "--verbose" in sys.argv

    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages
    )

    if verbose_flag:
        print("User prompt: ", prompt)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Generated tokens: ", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()