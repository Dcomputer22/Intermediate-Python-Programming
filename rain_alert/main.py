import requests
from twilio.rest import Client

MY_Endpoint = "https://api.weatherapi.com/v1/forecast.json?"
api_key = "8d87b8b605024b268f9104807232210"
account_sid = "ACd1dc0688e45f7f53e9fcdda464d9f1e2"
auth_token = "e16610529cedf7fac0c156a99ec3492e"

parameters = {
    "q": (6.852290, 7.395650),
    "key": api_key,
    "days": 1,
    "aqi": "no",
    "alerts": "no"
}
weather_response = requests.get(MY_Endpoint, params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
hourly_forecast = weather_data["forecast"]["forecastday"][0]["hour"][0:12]

will_rain = False

for data in hourly_forecast:
    condition_code = int(data["condition"]['code'])
    if condition_code >= 1006:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! Remember to take an Umbrella ☂️",
        from_="+17402364345",
        to="+23408069226824"
                )
