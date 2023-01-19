## Project 3 - Dictionary API with sqlite db 

from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

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
    # response =  {"usage":f"/dict?=<word>"}
    # return jsonify(response)
    return render_template("index.html")

@app.get('/dict')
def dictionary():
    
    words = request.args.getlist('word')
    
    if not words:
        response = {"status":"Error",'words':words, 'data':"word not found"}
        return jsonify(response)
    
    response = {'words':[]}
    
    for word in words:
        definitions = match_exact(word)
        if definitions:
            response['words'].append({"status":"Success","data":definitions,'word':word})
            # return jsonify(response)
        else:
            definitions = match_like(word)
            if definitions:
                response['words'].append({"status":"Partial","data":definitions,'word':word})
                # return jsonify(response)
            else:
                response['words'].append({"Status":"Error","data":"word not found"})
                # return jsonify(response)
    # return jsonify(response)     
    return render_template('results.html',response=jsonify(response))   


if __name__=='__main__':
    app.run()