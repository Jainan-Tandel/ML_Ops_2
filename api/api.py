from flask import Flask, request
app = Flask(__name__)

@app.route("/hello/<user>")
def hello_world(user):
    return f"<p>Hello {user}!</p>"

@app.route("/sum/<x>/<y>")
def sum(x,y):
    return str(int(x) + int(y))

@app.route("/model", methods=['POST'])
def pred_model():
    js = request.get_json()
    x = js['x']
    y = js['y']
    return str(int(x) + int(y))
