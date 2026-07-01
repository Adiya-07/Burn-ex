import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
data = pd.read_csv("../dataset/calories_dataset.csv")

# Convert text columns to numbers
exercise_encoder = LabelEncoder()
speed_encoder = LabelEncoder()

data["Exercise"] = exercise_encoder.fit_transform(data["Exercise"])
data["Speed"] = speed_encoder.fit_transform(data["Speed"])

# Features and target
X = data[["Exercise", "Speed", "Reps", "Duration", "Weight", "Height", "Age"]]
y = data["Calories"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", round(mae, 2))

# Save model
joblib.dump(model, "../model/calorie_model.pkl")

print("✅ Model trained successfully!")
print("✅ Model saved as calorie_model.pkl")