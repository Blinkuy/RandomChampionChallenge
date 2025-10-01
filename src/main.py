from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .core import add_character, drop_all, create_all, add_all, get_characters

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

@app.get("/")
def main_page(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})

@app.get("/character")
def character(request: Request):
    character = add_character()
    
    return templates.TemplateResponse(name="new_character.html", context={"request": request, "character_name": character})

@app.get("/character/all")
def get_all(request: Request):
    res = get_characters()
    
    return templates.TemplateResponse(name="all_characters.html", context={"request": request, "characters_list": res})

@app.get("/drop")
def drop():
    drop_all()
    create_all()
    add_all()
    
