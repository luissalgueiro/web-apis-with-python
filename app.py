## Project 4 - Image Filter API 

from flask import Flask, request, jsonify, send_file
# from model.dbHandler import match_exact, match_like
from bin.filters import apply_filter

### initialize the app ###
app = Flask(__name__)

## READ PIL documentation to find out the filters available



### Define what the app does ###
@app.route('/', methods=["GET","POST"])

def index():
    """
    ToDo:
    1. Return the usage instructions that specifies which filters are available and the method format
    """
    pass

    # return render_template("index.html")

@app.post('/<filter>')
def image_filter(filter):
    """
    ToDo: 
    1. Check if the provided filter is available,if not, return error
    2. Check if a file has been provided in the POST request., if not, return error
    3. Apply filter using apply_filter method imported from bin.filters 
    4. Return the filtered image
    """
   

if __name__=='__main__':
    app.run()