import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_directory.startswith(abs_working_directory) or not os.path.exists(abs_directory):
     return(f'Error: {directory} is not working direcotry.')
    
        

    final_response = "" 
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        if os.path.isfile(content_path):
            size = os.path.getsize(content_path)
            final_response += f"{content} - {size} bytes\n"
        elif os.path.isdir(content_path):
            final_response += f"{content}/ - Directory\n"    
    return final_response.strip()
 
 
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info", 
    description="Lists files and directories in a specified directory relative to the working directory, along with file sizes.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)    