import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
def main():
    # Load environment variables from .env file
    load_dotenv()
    print(os.getenv('GEMINI_API_KEY'))  # This will print your API key to confirm it's loaded correctly
   
    print(sys.version)  # This will print the Python version to confirm it's running in the correct environment
   # print(genai)  # This will print the version of the google-generativeai library to confirm it's installed correctly
    print(sys.argv)
    
    # Set your API key
    # Replace 'YOUR_API_KEY' with your actual Gemini API key
    
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    #client =  genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

   
    # Generate text
    if len(sys.argv) == 2:
        print(f"Generating content for prompt: {sys.argv[1]}")
        verbose = False
    elif len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"Generating content for prompt: {sys.argv[1]}")
        verbose = True
    else:
        print("No prompt provided.'")
        sys.exit(1)
        
    prompt = sys.argv[1];    

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=messages)


    print(response.text)
    if verbose:
        print(response.usage_metadata.prompt_token_count)
        print(response.usage_metadata.candidates_token_count)

if __name__ == "__main__":    
   # main()
   print(get_file_content("calculator", "test.py"))
   