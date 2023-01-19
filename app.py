## Project 4 - Image Filter API 

from flask import Flask, request, jsonify, send_file
# from model.dbHandler import match_exact, match_like
from bin.filters import apply_filter

### initialize the app ###
app = Flask(__name__)

## READ PIL documentation to find out the filters available
filters_available=[
    "blur",
    "contour",
    'edge_enhance',
    'edge_enhance_more'
]



### Define what the app does ###
@app.route('/', methods=["GET","POST"])

def index():
    """
    ToDo:
    1. Return the usage instructions that specifies which filters are available and the method format
    """
    response = {
        "filters_available":filters_available,
        "usage":{
            "http_method":"POST",
            "URL":"/<filters_available>"
        },
    }
    return jsonify(response)

    
@app.post('/<filter>')
def image_filter(filter):
    """
    ToDo: 
    1. Check if the provided filter is available,if not, return error
    2. Check if a file has been provided in the POST request., if not, return error
    3. Apply filter using apply_filter method imported from bin.filters 
    4. Return the filtered image
    """
    if filter not in filters_available:
        response = {"Error":"Unavailable filter"}
        return jsonify(response)
    
    file = request.files['image']
    if not file:
        response = {"Error":'File not found!'}
        return jsonify(response)
    
    filtered_image = apply_filter(file, filter)
    
    return send_file(filtered_image, mimetype="image/JPEG")
   

if __name__=='__main__':
    app.run()