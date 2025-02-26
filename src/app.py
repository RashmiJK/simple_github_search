from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Set the templates directory relative to the working directory (src/)
templates = Jinja2Templates(directory="src/templates")


@app.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/results", response_class=HTMLResponse)
async def get_results(request: Request):
    return templates.TemplateResponse("results.html", {"request": request})


# To run the app: uvicorn src.app:app --reload (run this command in the root folder)
