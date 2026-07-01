MEMBER 3:
# Burn-Ex
Burn-Ex is an AI-powered fitness calorie prediction system.

## Project Objective
The project detects user exercises using pose estimation and predicts the calories burned using a Machine Learning model.

## Features
- Exercise Detection
- Rep Counting
- Speed Detection
- Calorie Prediction
- Machine Learning Model

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- MediaPipe
- OpenCV

## Project Structure
Burn-ex/
│── dataset/
│   └── calories_dataset.csv
│
│── model/
│   └── calorie_model.pkl
│
│── training/
│   ├── generate_dataset.py
│   ├── train_model.py
│   └── predict.py
│
├── requirements.txt
└── README.md

## How to Run
Install the required packages:
```bash
pip install -r requirements.txt
```
Generate dataset:
```bash
python training/generate_dataset.py
```
Train the model:
```bash
python training/train_model.py
```
Run prediction:
```bash
python training/predict.py
```
## Member 3 Contribution
- Created calorie prediction dataset
- Built Machine Learning model
- Trained the model
- Saved trained model
- Developed calorie prediction module