from flask import Flask, jsonify, request

### initialize the app ###
app = Flask(__name__)

### Define what the app does ###
@app.get('/greet')
def index():
    # ## adding name as param for the API
    # name = request.args.get('name')
    # ## adding an error response in case the argument was not given properly
    # if not name:
    #     return jsonify({'status':'Error!'})
    # response = {'data':f'Hello {name}!!'}
    # ## When this direction is passing to the web browser, it generates the correct response
    # ### http://127.0.0.1:5000/greet?name=Luis 
    # ## ?var_name=var_value is the correct syntax
    
    """
    ToDo: 
    1. Capture first name and last name
    2. If either is not provided, return an error
    3. If first name is not provided and second name is provided, respond with "Hello, Mr/Miss <SecondName>!"
    4. If first name is provided and second name is not provided, respond with "Hello,  <FirstName>!"
    5. If both names are provided, respond with a question: "Is <FirstName> and <SecondName> your names?"
    
    """
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    if not fname and not lname:
        return jsonify({'status':'Error!'})
    elif lname and not fname:
        return jsonify({"data":f"Hello {lname}"})
    elif fname and not lname:
        return jsonify({"data":f"Hello {fname}"})
    else:
        return jsonify({"data":f" Is {fname} and {lname} your names?"})
    
    # return jsonify(response)

