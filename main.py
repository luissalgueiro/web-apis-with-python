from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses  import StreamingResponse
from typing import List, Optional
from model.dbHandler import match_exact, match_like
import io
from bin.filters import apply_filter


app = FastAPI()


filters_available=[
    "blur",
    "contour",
    "detail",
    "edge_enhance",
]


@app.api_route('/', methods=["GET","RESPONSE"])
def index():
    # response = {"Hello":"FastAPI"}
    response = {"filters_available":filters_available,
                "usage":{
                    "http_method":"POST",
                    "URL":"/<filter_available>/",
                }}
    return jsonable_encoder(response)

@app.post('/{filter}')
def image_filter(filter:str, img:UploadFile=File(...)):
    if filter not in filters_available:
        response = {"Error":"Filter not available"}
        return jsonable_encoder(response)
    
    filtered_image = apply_filter(img.file, filter)
    return StreamigResponse(filtered_image, media_type="image/jpeg")