from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from nasa.nasa_api import NasaAPI

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    nasa = NasaAPI()
    response = nasa.get_image().json()
    
    return templates.TemplateResponse("main.html", {"request": request, "data": response})
