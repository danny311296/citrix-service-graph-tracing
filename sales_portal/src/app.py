from flask import Flask

app = Flask(__name__)
@app.route('/')
def test():
    return 'Welcome to our Sales Portal Main Page'


