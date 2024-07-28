from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

    
@app.route("/home")
def home():
    return "<p>lets go guys</p>"

if __name__=='__main__':
    app.run(host="127.0.0.1",port=5000,debug=True)