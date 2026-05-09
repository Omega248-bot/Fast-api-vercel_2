from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"ano_actual": datetime.now().year},
    )


@app.get("/nosotros", response_class=HTMLResponse)
async def nosotros(request: Request):
    return templates.TemplateResponse(
        request=request, name="nosotros.html", context={"ano_actual": datetime.now().year},
    )

@app.get("/competencias", response_class=HTMLResponse)
async def competencias(request: Request):
    return templates.TemplateResponse(
        request=request, name="competencias.html", context={"ano_actual": datetime.now().year},
    )

@app.get("/patinetas", response_class=HTMLResponse)
async def patinetas(request: Request):
    return templates.TemplateResponse(
        request=request, name="patinetas.html", context={"ano_actual": datetime.now().year},
    )