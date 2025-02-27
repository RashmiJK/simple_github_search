from typing import Annotated

import requests
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Set the templates directory relative to the working directory (src/)
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/search_results", response_class=HTMLResponse)
def get_results(request: Request, search_keywords: Annotated[str, Form(...)]):
    print(f"search_keywords: {search_keywords}")
    # Call GitHub API to search for repositories
    response = requests.get(f"https://api.github.com/search/repositories?q={search_keywords}")
    search_results = response.json().get("items", [])
    return templates.TemplateResponse(
        "results.html", {"request": request, "search_keywords": search_keywords, "search_results": search_results}
    )
