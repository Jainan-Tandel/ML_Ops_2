from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=["POST"])
def hello_world_post():    
    return {"op" : "Hello, World POST " + request.json["suffix"]}

@app.route("/sum/<x>/<y>")
def sum(x,y):
    return str(int(x) + int(y))

@app.route("/model", methods=['POST'])
def pred_model():
    js = request.get_json()
    image = np.array(js['image'])
    image.reshape(1,-1)
    model = joblib.load('models/svm_gamma:0.001_C:1.joblib')
    predict = model.predict([image])
    return str(predict)

@app.route("/compare", methods=['POST'])
def compare_images():
    js = request.get_json()
    image1 = np.array(js['image1'])
    image2 = np.array(js['image2'])

    image1.reshape(1, -1)
    image2.reshape(1, -1)
    model = joblib.load('models/svm_gamma:0.001_C:1.joblib')
    predict = model.predict([image1,image2])
    # predict2 = model.predict(image2)

    if( (predict[0] == predict[1])):
        return f"True"
    else:
        return f"False"

if __name__ == "__main__":
    app.run(host="0.0.0.0")