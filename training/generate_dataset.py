import csv
import random

exercises = [
    ("Squat", [10, 15, 20], [18, 22, 25]),
    ("Jumping_Jack", [10, 20, 30], [20, 25, 30]),
    ("High_Knees", [0], [20, 30])
]

speeds = ["Slow", "Normal", "Fast"]

with open("../dataset/calories_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Exercise",
        "Speed",
        "Reps",
        "Duration",
        "Weight",
        "Height",
        "Age",
        "Calories"
    ])

    for i in range(100):

        exercise, reps_list, duration_list = random.choice(exercises)

        speed = random.choice(speeds)
        reps = random.choice(reps_list)
        duration = random.choice(duration_list)

        weight = random.randint(50, 90)
        height = random.randint(150, 190)
        age = random.randint(18, 35)

        # Simple calorie estimation
        base = duration * 0.15 + reps * 0.30

        if exercise == "Squat":
            base += 2
        elif exercise == "Jumping_Jack":
            base += 3
        else:
            base += 4

        if speed == "Normal":
            base *= 1.1
        elif speed == "Fast":
            base *= 1.25

        calories = round(base + weight * 0.03, 2)

        writer.writerow([
            exercise,
            speed,
            reps,
            duration,
            weight,
            height,
            age,
            calories
        ])

print("✅ 100 rows generated successfully!")