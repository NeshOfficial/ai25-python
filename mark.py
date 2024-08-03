# markresolve.py

import os

def read_issues(file_path):
    """
    Reads issues from a file and returns them as a list of strings.
    :param file_path: Path to the file containing issues.
    :return: List of issues.
    """
    if not os.path.isfile(file_path):
        return [], f"Error: {file_path} does not exist."

    try:
        with open(file_path, 'r') as file:
            issues = file.readlines()
        return issues, None
    except Exception as e:
        return [], f"Error reading file: {e}"

def write_issues(file_path, issues):
    """
    Writes a list of issues to a file.
    :param file_path: Path to the file.
    :param issues: List of issues to write.
    """
    try:
        with open(file_path, 'w') as file:
            file.writelines(issues)
    except Exception as e:
        print(f"Error writing to file: {e}")

def mark_resolved(issues, issue_number):
    """
    Marks an issue as resolved by adding '(Resolved)' to it.
    :param issues: List of issues.
    :param issue_number: The issue number to mark as resolved.
    :return: Updated list of issues.
    """
    try:
        issues[issue_number - 1] = issues[issue_number - 1].strip() + " (Resolved)\n"
    except IndexError:
        print(f"Error: Issue number {issue_number} does not exist.")
    return issues

def main():
    """
    Main function to execute the script.
    """
    file_path = input("Enter the path to the issues file: ")
    issues, error = read_issues(file_path)
    
    if error:
        print(error)
        return
    
    try:
        issue_number = int(input("Enter the issue number to mark as resolved: "))
        issues = mark_resolved(issues, issue_number)
        write_issues(file_path, issues)
        print(f"Issue {issue_number} marked as resolved.")
    except ValueError:
        print("Error: Please enter a valid issue number.")

if __name__ == "__main__":
    main()
