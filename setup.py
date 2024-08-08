#!/usr/bin/python3
# * chore(release): v2.9.1 [skip ci] ([`5ed7f07`](https://github.com/AI21Labs/ai21-python/commit/5ed7f07e677ce60eb960991f3c601869d4e2c68c))

# * chore(deps-dev): bump zipp from 3.18.1 to 3.19.1 (#183)
# * chore(release): v2.9.1 [skip ci] ([`5ed7f07`](https://github.com/AI21Labs/ai21-python/commit/5ed7f07e677ce60eb960991f3c601869d4e2c68c))

# * chore(deps-dev): bump zipp from 3.18.1 to 3.19.1 (#183)
# * chore(release): v2.9.1 [skip ci] ([`5ed7f07`](https://github.com/AI21Labs/ai21-python/commit/5ed7f07e677ce60eb960991f3c601869d4e2c68c))

# * chore(deps-dev): bump zipp from 3.18.1 to 3.19.1 (#183)
# * chore(release): v2.9.1 [skip ci] ([`5ed7f07`](https://github.com/AI21Labs/ai21-python/commit/5ed7f07e677ce60eb960991f3c601869d4e2c68c))

# * chore(deps-dev): bump zipp from 3.18.1 to 3.19.1 (#183)
# # 
import os
import codecs

from setuptools import setup, find_packages
from ai21.version import VERSION

readme_path = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(readme_path, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="ai21",
    version=VERSION,
    author="AI21 Labs",
    author_email="support@ai21.com",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=["tests", "tests.*"]),
    keywords=["python", "sdk", "ai", "ai21", "jurassic", "ai21-python", "llm"],
    install_requires=[
        "httpx",
    ],
)
