from fastapi import FastAPI
from fastapi import jsonable_encoder
from typing import Optional
from model.dbHandler import match_exact, match_like



app = FastAPI()


@app.get('/')
def index():
    # response = {"Hello":"FastAPI"}
    response = {'usage':'/dict?=<word>'}
    return jsonable_encoder(response)

@app.get('/dict')
def dict(word:str):
    if not word:
        response = {'status':'Error','word':word,'data':'Word Not Found!'}
        return jsonable_encoder(response)
    definitions = match_exact(word)
    if definitions:
        response = {'status':'success','word':word,'data':definitions}
        return jsonable_encoder(response)
    else:
        definitions = match_like(word)
        if definitions:
            response = {'status':'partial','word':word,'data':definitions}
            return jsonable_encoder(response)
        else:
            response = {'status':'Error','word':word,'data':"Word without definition"}
            return jsonable_encoder(response)
    