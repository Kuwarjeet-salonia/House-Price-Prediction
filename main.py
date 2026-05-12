from flask import Flask , render_template , request
import joblib
# import numpy as np  
import torch
import torch.nn as nn
model = nn.Linear(4,1)
checkpoint = torch.load("model.pth")
model.load_state_dict(checkpoint["model_state"])
X_mean = checkpoint["Xmean"]
X_std = checkpoint["Ystd"]
Y_mean = checkpoint["Ymean"]
Y_std = checkpoint["Ystd"]
model.eval()
app =  Flask(__name__)
model = joblib.load("model.pkl")
@app.route("/",methods=["GET","POST"])
def home():
    prediction = None
    if request.method == "POST":
        area =  float(request.form["area"])
        bedrooms =  int(request.form["bedrooms"])
        bathrooms =  int(request.form["bathrooms"])
        age =  int(request.form["age"])
        features = torch.tensor([[area,bedrooms,bathrooms,age]],
                                dtype=torch.float32
                                )
        features = (
            features - X_mean
        ) / (X_std + 1e-8)
        with torch.no_grad():
            prediction=model(features)
            prediction = prediction*Y_std+Y_mean
        prediction = round(prediction.item(),2)
    [0]
    return render_template("main.html",prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True)