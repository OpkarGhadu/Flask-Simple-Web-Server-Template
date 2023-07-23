# Simple Python Web Server using Flask
# 
# Note : Only for development. For production use
#   WSGI Server
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Static Pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Dynamic Pages
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)
