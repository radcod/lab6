import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# dummy dataset
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

# evaluate
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)

# save model
joblib.dump(model, "model.pkl")

# save metrics
metrics = {"mse": float(mse)}
with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print("Training complete. MSE:", mse)