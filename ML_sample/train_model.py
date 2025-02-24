import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Generate sample dataset
data = pd.DataFrame({
    "square_feet": np.random.randint(500, 5000, 1000),
    "bedrooms": np.random.randint(1, 6, 1000),
    "bathrooms": np.random.randint(1, 4, 1000),
    "location": np.random.choice(["urban", "suburban", "rural"], 1000),
    "price": np.random.randint(100000, 1000000, 1000)
})

# One-hot encode categorical feature (location)
data = pd.get_dummies(data, columns=["location"], drop_first=True)

# Split data
X = data.drop("price", axis=1)
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")

# Save the trained model
joblib.dump(model, "house_price_model.pkl")

# Save the column names for input validation
joblib.dump(X_train.columns.tolist(), "model_features.pkl")

print("Model training complete. Files saved!")
