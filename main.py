import os
import google.generativeai as genai
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()
    print(os.getenv('GEMINI_API_KEY'))  # This will print your API key to confirm it's loaded correctly
    # Set your API key
    # Replace 'YOUR_API_KEY' with your actual Gemini API key
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

    # Create the model
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Generate text
    response = model.generate_content('How is the weather today?')


    print(response.text)
    print(response.usage_metadata.prompt_token_count)
    print(response.usage_metadata.candidates_token_count)

if __name__ == "__main__":    
    main()