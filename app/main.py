import traceback

from flask import Flask, request, jsonify
from flask.templating import render_template

from app.torch_utils import transform_image, get_prediction


app = Flask(__name__)


def get_class(class_id):
    class_list = [
        "plane",
        "car",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck",
    ]
    if class_id < 0 or class_id > len(class_list) - 1:
        return None
    return class_list[class_id]


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]
        if file is None or file.filename == "":
            return jsonify({"error": "No file provided"})

        if not allowed_file(file.filename):
            return jsonify({"error": "Image format not supported"})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            score, prediction = get_prediction(tensor)
            data = {
                "class": get_class(prediction.item()),
                "score": round(score * 100, 2),
            }
            return jsonify(data)
        except:
            traceback.print_exc()
            return jsonify({"error": "Error during prediction"})
