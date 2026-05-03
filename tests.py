from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
def test_get_files_info():
    # Test with a valid directory
    result = get_files_info("calculator")
    assert "main.py" in result  

    # Test with a subdirectory
    result = get_files_info("calculator", "pkg")
    assert "calculator.py" in result

    # Test with an invalid directory
    result = get_files_info("calculator", "non_existent_directory")
    assert "Error" in result

    # Test with a directory that is not a subdirectory of the working directory
    result = get_files_info("calculator", "../")
    assert "Error" in result


def test_get_file_content():
    # Test with a valid file
    result = get_file_content("calculator", "main.py")
    assert "main" in result  

    # Test with an invalid file
    result = get_file_content("calculator", "non_existent_file.py")
    assert "Error" in result

    # Test with a file that is not within the working directory
    result = get_file_content("calculator", "../main.py")
    assert "Error" in result
    
    result = get_file_content("calculator", "pkg/calculator.py")
    assert "class Calculator" in result

def test_write_file():
    # Test writing to a valid file
    result = write_file("calculator", "test_write.txt", "Hello, World!")
    assert "Successfully wrote" in result

    # Test writing to a file outside the working directory
    result = write_file("calculator", "../test_write.txt", "Hello, World!")
    assert "Error" in result
    
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    assert "Successfully wrote" in result
    result =write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    assert "Successfully wrote" in result
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    assert "Error" in result

def test_run_python_file():
    # Test running a valid Python file
    result = run_python_file("calculator", "main.py", args=["3 + 5"])
    print(result)
    assert "Successfully executed" in result

    # Test running a Python file outside the working directory
    result = run_python_file("calculator", "../main.py")
    print(result)
    assert "Error" in result
    
if __name__ == "__main__":
    test_get_files_info()
    test_get_file_content()
    test_write_file()
    test_run_python_file()
    print("All tests passed!")