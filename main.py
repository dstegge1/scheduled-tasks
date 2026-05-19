import requests
import smtplib
import os

weather_api_key = os.environ.get("WEATHER_API_KEY")
my_email = os.environ.get("MY_EMAIL")
to_email = os.environ.get("TO_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

url = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 39.2905,
    "lon": -76.6104,
    "appid": weather_api_key,
    "cnt": 4
}

will_rain = False

response = requests.get(url, params= weather_params)
response.raise_for_status()
weather_data = response.json()
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Will Rain")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = to_email,
            msg = ("Subject: Bring Umbrella:\n\n"
                   "Bring your umbrella today as it will rain!")
        )
else:
    print("Not rain")
