import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
import numpy as np
import pandas as pd
 
scaler = StandardScaler()
def to_string_func(x):
    return x.astype(str)
 
app = Flask(__name__)
model = pickle.load(open('new_model.pkl','rb'))
 
@app.route('/')
def home():
    return render_template("home.html")
 
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    # Create DataFrame directly
    df = pd.DataFrame([data])
    print(df)
    output = model.predict(df)
    print(output[0])
    return jsonify(output[0])
 
@app.route('/predict',methods=['POST'])
def predict():
    try:
        fields = ['kitchen_area','bath_area','other_area','extra_area',
    'extra_area_count','year','ceil_height','floor_max',
    'floor','total_area','bath_count','rooms_count']
        
        data = request.form.to_dict()
 
        df = pd.DataFrame([data])
 
        print(df)

        for field in fields:
            value = request.form.get(field)

            try:
                if float(value) <= 0:
                    return render_template(
                        "home.html",
                        prediction_text="All values must be non-zero and positive"
                    )
            except:
                return render_template(
                    "home.html",
                    prediction_text=f"Invalid input in {field}"
                )
 
        output = model.predict(df)[0]
 
        return render_template(
            "home.html",
            prediction_text=f"House Price is {output}"
        )
 
    except Exception as e:
        return str(e)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)