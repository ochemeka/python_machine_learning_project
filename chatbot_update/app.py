from flask import Flask, render_template, request, jsonify

# from flask import CORS
from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #check is error is valid
    response  = get_response(text)
    message = {"answer": response}  #we use a dictionary here
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
#now we start running our application file

