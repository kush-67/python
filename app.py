
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("iris_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        try:
            sepal_length = float(request.form["sepal_length"])
            sepal_width = float(request.form["sepal_width"])
            petal_length = float(request.form["petal_length"])
            petal_width = float(request.form["petal_width"])
            data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            pred = model.predict(data)[0]
            classes = ["Setosa", "Versicolor", "Virginica"]
            prediction = f"Predicted Iris Species: {classes[pred]}"
        except:
            prediction = "Invalid input. Please enter valid numbers."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
