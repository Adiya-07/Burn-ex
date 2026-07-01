import joblib
import pandas as pd

# Load trained model
model = joblib.load("../model/calorie_model.pkl")

# Same encoding as train_model.py
exercise_map = {
    "Squat": 0,
    "Jumping_Jack": 1,
    "High_Knees": 2
}

speed_map = {
    "Slow": 2,
    "Normal": 1,
    "Fast": 0
}

print("===== Burn-Ex Calorie Predictor =====")

exercise = input("Exercise (Squat/Jumping_Jack/High_Knees): ")
speed = input("Speed (Slow/Normal/Fast): ")
reps = int(input("Reps: "))
duration = int(input("Duration (seconds): "))
weight = int(input("Weight (kg): "))
height = int(input("Height (cm): "))
age = int(input("Age: "))

data = pd.DataFrame([[
    exercise_map[exercise],
    speed_map[speed],
    reps,
    duration,
    weight,
    height,
    age
]], columns=[
    "Exercise",
    "Speed",
    "Reps",
    "Duration",
    "Weight",
    "Height",
    "Age"
])

prediction = model.predict(data)

print(f"\n🔥 Estimated Calories Burned: {prediction[0]:.2f} kcal")