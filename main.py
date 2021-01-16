import requests
from datetime import datetime
import os


APP_ID = os.environ["APP_ID"]
GENDER = "male"
API_KEY = os.environ["API_KEY"]
WEIGHT = 65.5
HEIGHT = 154
AGE = 31

BASIC_AUTH = os.environ["BASIC_AUTH"]
BEARER_AUTH = os.environ["BEARER_AUTH"]

exercise_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("Tell me which exercise you did: ")
exercise_body_param = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_body_param, headers=exercise_headers)
print(response.text)
print(response.status_code)
result = response.json()
exercise = result["exercises"][0]["user_input"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
# date = datetime.now()
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

print(exercise)
print(duration)
print(calories)
print(date)
print(time)

sheety_endpoint = "https://api.sheety.co/db496232a34cbde872578557c491d899/workoutTracking/workouts"
# headers = {
#     "Authorization": f"Basic {BASIC_AUTH}}"
# }

headers = {
    "Authorization": f"Bearer {BEARER_AUTH}",
}
for exercise in result["exercises"]:
    sheety_param = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(url=sheety_endpoint,
                                    json=sheety_param,
                                    headers=headers)
    print(sheety_response.text)
