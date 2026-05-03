import os
import sys
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

working_directory = "calculator"

def call_function(function_call_part,verbose=False):
    if verbose:
        print(f"Function name: {function_call_part.name}")
        print(f"Arguments: {function_call_part.args}")
        
        
    try:     
        if function_call_part.name == "get_files_info":
            directory = function_call_part.args.get("directory", ".")
            return get_files_info(working_directory, **function_call_part.args)
        if function_call_part.name == "get_file_content":
            file_path = function_call_part.args.get("file_path")
            return get_file_content(working_directory, file_path)
        if function_call_part.name == "write_file":
            file_path = function_call_part.args.get("file_path")
            content = function_call_part.args.get("content")
            return write_file(working_directory, file_path, content)
        if function_call_part.name == "run_python_file":
            file_path = function_call_part.args.get("file_path")
            args = function_call_part.args.get("args", [])
            return run_python_file(working_directory, file_path, args)
    except Exception as e:
       return types.Content(role="tool", parts=[types.Part.from_function_response(name=function_call_part.name, text=f"Error: Unrecognized function {function_call_part.name}")])