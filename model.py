# import libraries
import pandas as pd 
import torch
import torch.optim as optim
import torch.nn as nn
from sklearn.linear_model import LinearRegression
import joblib
# load data
df = pd.read_csv("house_data.csv")
X_pd= df[["area","bedrooms","bathrooms","age"]]
Y_pd = df[["price"]]
# convert tensor
V = torch.tensor(X_pd.values,dtype=torch.float32)
W = torch.tensor(Y_pd.values,dtype=torch.float32)
X = (V - V.mean(dim=0)) / (V.std(dim=0) +1e-8)
Y = (W - W.mean(dim=0)) / (W.std(dim=0) +1e-8)
# model
model = nn.Linear(4,1)
optimizer = torch.optim.Adam(model.parameters(),lr=0.0001)
loss_fn = nn.MSELoss()
# training and learning
for epoch in range(10000):
    pred = model(X)
    loss = loss_fn(pred,Y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
X_mean = V.mean(dim=0)
X_std = V.std(dim=0)
Y_mean = W.mean()
Y_std = W.std()

torch.save({
    "model_state": model.state_dict(),
    "Xmean": X_mean,
    "Ystd": X_std,
    "Ymean":Y_mean,
    "Ystd":Y_std
}, "model.pth")
# save 
joblib.dump(model,"model.pkl")
print("model trained successfully")
