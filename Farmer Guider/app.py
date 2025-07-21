from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load(r"C:\Users\PARIMAL\OneDrive\Desktop\Projects\Farmer Guider\model_compressed.lb")

prediction_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            N = int(request.form['N'])
            P = int(request.form['P'])
            K = int(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
            prediction_code = model.predict(input_data)[0]

            crop_map = {
                0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans',
                4: 'pigeonpeas', 5: 'mothbeans', 6: 'mungbean', 7: 'blackgram',
                8: 'lentil', 9: 'pomegranate', 10: 'banana', 11: 'mango',
                12: 'grapes', 13: 'watermelon', 14: 'muskmelon', 15: 'apple',
                16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton',
                20: 'jute', 21: 'coffee'
            }

            prediction = crop_map.get(prediction_code, "Unknown Crop")

            prediction_history.append((prediction, N, P, K, temperature, humidity, ph, rainfall))

            return render_template("predict.html", prediction=prediction)
        except Exception as e:
            return f"Error: {e}"

    return render_template("predict.html", prediction=None)


@app.route("/history")
def history():
    return render_template("history.html", historical_data=prediction_history)

if __name__ == "__main__":
    app.run(debug=True)
