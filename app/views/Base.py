import os

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import settings


ViewsRouter = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@ViewsRouter.get('/test', response_class=HTMLResponse)
async def test_html(request: Request):
    print(os.getcwd())
    return templates.TemplateResponse('index.html', {'request': request})
