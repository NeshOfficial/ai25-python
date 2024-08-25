#!/usr/bin/python3

import os
import codecs


from ai21.version import VERSION

readme_path = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(readme_path, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

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

