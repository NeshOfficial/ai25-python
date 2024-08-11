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
import math

def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    return sum(data) / len(data)

def calculate_variance(data, mean):
    """Calculate the variance of a list of numbers."""
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_stddev(data):
    """Calculate the standard deviation of a list of numbers."""
    mean = calculate_mean(data)
    variance = calculate_variance(data, mean)
    stddev = math.sqrt(variance)
    return stddev

def read_data_from_file(filename):
    """Read a list of numbers from a file."""
    with open(filename, 'r') as file:
        data = [float(line.strip()) for line in file]
    return data

def write_results_to_file(filename, mean, stddev):
    """Write the mean and standard deviation to a file."""
    with open(filename, 'w') as file:
        file.write(f"Mean: {mean}\n")
        file.write(f"Standard Deviation: {stddev}\n")

def main():
    input_file = 'data.txt'
    output_file = 'results.txt'

    # Read data from file
    data = read_data_from_file(input_file)

    # Calculate mean and standard deviation
    mean = calculate_mean(data)
    stddev = calculate_stddev(data)

    # Print results to console
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {stddev}")

    # Write results to file
    write_results_to_file(output_file, mean, stddev)

    # Additional functionality: Check if standard deviation is within a threshold
    threshold = 10.0
    if stddev > threshold:
        print(f"Warning: Standard deviation exceeds the threshold of {threshold}.")

if __name__ == "__main__":
    main()
