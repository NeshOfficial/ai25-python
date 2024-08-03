# reader.py

import os

def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    if not os.path.isfile(file_path):
        return f"Error: {file_path} does not exist."

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"

def print_file_content(file_path):
    """
    Reads the content of a file and prints it to the console.
    :param file_path: Path to the file to be read.
    """
    content = read_file(file_path)
    print(content)

def main():
    """
    Main function to execute the script.
    """
    file_path = input("Enter the path to the file you want to read: ")
    print_file_content(file_path)

if __name__ == "__main__":
    main()
