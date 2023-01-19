## Project 3 - Dictionary API with sqlite db 

from flask import Flask, request, jsonify, render_template
from model import match_exact, match_like

### initialize the app ###
app = Flask(__name__)

### Define what the app does ###
@app.get('/')
def index():
    """
    Provide instructions for the usage 
    Returns:
        response: json formatted
    """
    response =  {"usage":f"/dict?{word}"}
    return jsonify(response)

@app.get('/dict')
def dictionary():
    
    word= request.args.get('word')
    
    if not word:
        return jsonify({"status":"Error", 'data':"word not found"})
    
    definitions = match_exact(word)
    if definitions:
        return jsonify({"status":"Success","data":definitions})
    
    definitions = match_like(word)
    if definitions:
        return jsonify({"status":"Partial","data":definitions})
    else:
        return jsonify("Status":"Error","data":"word not found")
    


if __name__=='__main__':
    app.run()