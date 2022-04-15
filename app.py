from cgitb import text
from email import message
from urllib import response
from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO:check if it is valid

    response,exam = get_response(text)
    msg = {"answer":response}
    if exam:
        import webbrowser
        webbrowser.open(msg["answer"])
    else:        
        return jsonify(msg)

if __name__ == "__main__":
    app.run(debug=True)

