from flask import Flask

app = Flask(__name__)

@app.route('/')
def hey():
    return 'yveslym'

if __name__=="__main__":
    app.run()
