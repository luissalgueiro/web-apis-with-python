## Project 2 - Web Browser Google alike using the Google API 


from flask import Flask, request, render_template, redirect

### initialize the app ###
app = Flask(__name__)

### Define what the app does ###
@app.get('/')
def index():
    return render_template('index.html')

@app.get('/search')
def search():
    args = request.args.get('q')
    return redirect(f'https://www.google.com/search?q={args}')

if __name__=='__main__':
    app.run()