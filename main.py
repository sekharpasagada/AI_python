import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv
import call_function
from functions.get_files_info import get_files_info,schema_get_files_info
from functions.get_file_content import get_file_content,schema_get_file_content
from functions.write_file import write_file,schema_write_file
from functions.run_python_file import run_python_file,schema_run_python_file
from prompts import system_prompt
from call_function import call_function
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

    available_functions = types.Tool( function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],)
        

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]
    config=types.GenerateContentConfig(system_instruction=system_prompt,tools=[available_functions])
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=messages,config=config, )


    


    if response.function_calls:
        print("Function calls made by the model:")
        for call in response.function_calls:
          result = call_function(call, verbose)
          print(f"Result of {call.name}: {result}")
    else:
        print("No function calls were made by the model.")  
        print(response.text) 
    if verbose:
        print(response.usage_metadata.prompt_token_count)
        print(response.usage_metadata.candidates_token_count)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages,
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":    
    main()
   