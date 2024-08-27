# # import string
# # import random
# # import os

# <<<<<<< slider-component

# ingest_data and process_data cannot process multiple file/url arguments. Specify 1 at a time.
# Use process_data to process large amounts of data with a larger context window.
# Python code run with execute_python must end with an output "print" statement.
# Do not search the web for information that GPT3/GPT4 already knows.
# Use memorize_thoughts to organize your thoughts.
# memorize_thoughts argument must not be empty!
# Send the "done" command if the objective was achieved.
# RESPOND WITH EXACTLY ONE THOUGHT/COMMAND/ARG COMBINATION.
# DO NOT CHAIN MULTIPLE COMMANDS.
# NO EXTRA TEXT BEFORE OR AFTER THE COMMAND.
# DO NOT REPEAT PREVIOUSLY EXECUTED COMMANDS.

# Each action returns an observation. Important: Observations may be summarized to fit into your limited memory.

# Example actions:

# <r>Think about skills and interests that could be turned into an online job.</r><c>memorize_thoughts</c>
# I have experience in data entry and analysis, as well as social media management.
# (...)

# <r>Search for websites with chocolate chip cookies recipe.</r><c>web_search</c>
# chocolate chip cookies recipe

# <r>Ingest information about chocolate chip cookies.</r><c>ingest_data</c>
# https://example.com/chocolate-chip-cookies

# <r>Read the local file /etc/hosts.</r><c>ingest_data</c>
# /etc/hosts

# <r>Extract information about chocolate chip cookies.</r><c>process_data</c>
# Extract the chocolate cookie recipe|https://example.com/chocolate-chip-cookies

# <r>Summarize this Stackoverflow article.</r><c>process_data</c>
# Summarize the content of this article|https://stackoverflow.com/questions/1234/how-to-improve-my-chatgpt-prompts

# <r>Review this code for security issues.</r><c>process_data</c>
# Review this code for security vulnerabilities|/path/to/code.sol

# <r>I need to ask the user for guidance.</r><c>talk_to_user</c>
# What is the URL of a website with chocolate chip cookies recipes?

# <r>Write 'Hello, world!' to file</r><c>execute_python</c>
# with open('hello_world.txt', 'w') as f:
#     f.write('Hello, world!')

# <r>The objective is complete.</r><c>done</c>
# '''

# CRITIC_PROMPT = '''
# You are a critic reviewing the actions of an autonomous agent.

# Evaluate the agent's performance. It should:
# - Make real-world progress towards the objective
# - Take action instead of endlessly talking to itself
# - Not perform redundant or unnecessary actions
# - Not attempt actions that cannot work (e.g. watching a video)
# - Not keep repeating the same command
# - Communicate results to the user

# Make concise suggestions for improvements.
# Provide recommended next steps.
# Keep your response as short as possible.

# EXAMPLE:

# Criticism: You have been pretending to order pizza but have not actually
# taken any real-world action. You should course-correct.

# Recommended next steps:

# 1. Request an Uber API access token from the user.
# 2. Use the Uber API to order pizza.

# AGENT OBJECTIVE:

# {objective}

# AGENT HISTORY:

# {context}


# =======
# # <<<<<<< visualization

# # from ai21.version import VERSION
# # =======
# # # Function to generate a difficult file name
# # def generate_difficult_filename(length=50):
# #     characters = string.ascii_letters + string.digits + string.punctuation
# #     return ''.join(random.choice(characters) for _ in range(length))

# Function to write 50 lines to a file
def write_lines_to_file(filename, num_lines=50):
    with open(filename, 'w') as file:
        for i in range(1, num_lines + 1):
            file.write(f'This is line number {i}\n')

# Generate a difficult file name
difficult_filename = generate_difficult_filename()


# Ensure the file is saved in a safe location
safe_directory = os.path.expanduser('~/difficult_files')
os.makedirs(safe_directory, exist_ok=True)
file_path = os.path.join(safe_directory, difficult_filename)

# Write 50 lines to the file
write_lines_to_file(file_path)


# first(    name="ai21",
    version=VERSION,
    author="AI21 Labs",
    author_email="support@ai21.com",
    long_description_content_type="text/markdown",
    long_description=long_description,
   
    keywords=["python", "sdk", "ai", "ai21", "jurassic", "ai21-python", "llm"],
    install_requires=[
        "httpx",
    ],

