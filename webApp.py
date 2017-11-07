from flask import Flask


app = Flask(__name__)
# api = Api(app)

@app.route('/')
def hey():
    return 'yveslym'
