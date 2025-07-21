from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load(r"C:\Users\PARIMAL\OneDrive\Desktop\Projects\Laptop Price\model_compressed.lb")

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

@app.route("/project", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        
            
            brand = int(request.form['brand'])
            processor_brand = int(request.form['processor_brand'])
            processor_name = int(request.form['processor_name'])
            processor_gnrtn = int(request.form['processor_gnrtn'])
            ram_gb = int(request.form['ram_gb'])
            ssd = int(request.form['ssd'])
            hdd = int(request.form['hdd'])
            os = int(request.form['os'])
            os_bit = int(request.form['os_bit'])
            graphic_card_gb = int(request.form['graphic_card_gb'])
            ratings = int(request.form['ratings'])
            reviews = int(request.form['reviews'])

            input_data = [[
                brand, processor_brand, processor_name,
                processor_gnrtn, ram_gb, ssd, hdd,
                os, os_bit, graphic_card_gb,
                ratings, reviews
            ]]


            prediction = int(model.predict(input_data)[0])

            prediction_history.append((
                prediction, brand, processor_name, ram_gb, ratings, reviews
            ))

            return render_template("project.html", prediction=prediction)

        

    return render_template("project.html", prediction=None)

@app.route("/history")
def history():
    return render_template("history.html", historical_data=prediction_history)

if __name__ == "__main__":
    app.run(debug=True)
