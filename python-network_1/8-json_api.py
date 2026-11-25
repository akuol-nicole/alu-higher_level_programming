#!/usr/bin/python3
"""Sends a POST request to search_user with a letter and parses JSON output."""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        json_res = r.json()
        if json_res:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
