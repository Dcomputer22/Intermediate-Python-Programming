import requests
from datetime import datetime
import os

APP_ID = "ce63b0b8"
APP_API = os.environ["APPLICATION_API"]
GENDER = "Female"
WEIGHT_KG = "59"
HEIGHT = "6.5"
AGE = "21"

app_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1ed6c7c7fe694123f859f854d236c67d/myWorkoutTracker/workouts"
print(APP_API)
exercise_query = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_API,
}
app_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height": HEIGHT,
    "age": AGE,
}

response = requests.post(url=app_endpoint, json=app_params, headers=headers)
response_result = response.json()
print(response_result)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in response_result["exercises"]:
    sheet_inputs = {
        "workouts": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
