import os

import requests
from dotenv import load_dotenv


def load_envs():
    def find_dotenv_file():
        path = os.path.dirname(__file__)
        while path:
            dotenv_path = os.path.join(path, ".env")
            if os.path.exists(dotenv_path):
                return dotenv_path
            parent = os.path.dirname(path)
            if parent == path:  # Stop at root directory
                break
            path = parent
        return None

    dotenv_path = find_dotenv_file()
    if dotenv_path:
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError("No .env file found in the workspace")


def search_github_repositories(search_keywords: str):
    load_envs()

    headers = {
        "Authrization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }

    params = {
        "q": search_keywords,
        "sort": "stars",
        "order": "desc",
        "per_page": 20,
    }

    response = requests.get("https://api.github.com/search/repositories", headers=headers, params=params)

    if response.status_code == 200:
        return response.json()["items"]
    else:
        return []
