from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.git_search import search_github_repositories

app = FastAPI()

# Set the templates directory relative to the working directory (src/)
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    error = request.query_params.get("error")
    return templates.TemplateResponse("home.html", {"request": request, "error": error})


@app.post("/search_results", response_class=HTMLResponse)
def get_results(request: Request, search_keywords: Annotated[str, Form(...)]):
    if not search_keywords:
        return templates.TemplateResponse("home.html", {"request": request, "error": "Please enter some keywords."})
    print(f"search_keywords: {search_keywords}")
    # issue search request
    search_results = search_github_repositories(search_keywords)
    return templates.TemplateResponse(
        "results.html", {"request": request, "search_keywords": search_keywords, "search_results": search_results}
    )
