from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .nasa.nasa_api import NasaAPI

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def render_page(request: Request):
    nasa = NasaAPI()
    response = nasa.get_image().json()
    
    return templates.TemplateResponse("main.html", {"request": request, "data": response})


@app.get("/nasa-image")
async def get_image(date: str):
    nasa = NasaAPI()
    response = nasa.get_image(date).json()
    
    return response