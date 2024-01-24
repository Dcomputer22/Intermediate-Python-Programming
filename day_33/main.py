import requests
from datetime import datetime

MY_LAT = 6.852290
MY_LONG = 7.395650
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()
# #
# # stat_code = response.status_code
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

time_now = datetime.now()
print(time_now.hour)
