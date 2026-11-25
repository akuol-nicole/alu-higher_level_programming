#!/usr/bin/python3
"""Uses the GitHub API with Basic Auth to display your GitHub user id."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get("https://api.github.com/user", auth=(username, token))
    print(r.json().get("id"))
