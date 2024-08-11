import string
import subprocess

def check_palindrome(input_string):
    # Normalize the input: remove spaces, punctuation, and convert to lowercase
    normalized_string = ''.join(
        char.lower() for char in input_string if char.isalnum()
    )

    # Reverse the string
    reversed_string = normalized_string[::-1]

    # Check if the original string is equal to the reversed string
    if normalized_string == reversed_string:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def run_git_commands():
    # Initialize a Git repository
    subprocess.run(["git", "init"], check=True)

    # Add the script to the repository
    subprocess.run(["git", "add", "palindrome_script.py"], check=True)

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Added palindrome check script"], check=True)

    # Pull the latest changes from the remote repository to avoid conflicts
    subprocess.run(["git", "pull", "origin", "main"], check=True)

    # Push the changes to the GitHub repository
    subprocess.run(["git", "push", "origin", "main"], check=True)

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter a string to check if it's a palindrome: ")
    check_palindrome(user_input)

    # Run Git operations
    run_git_commands()
