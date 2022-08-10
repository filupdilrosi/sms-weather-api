import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b239ad6816f4e09d41069588e7ac2d80"
account_sid = "AC3585ff852a3397fae134d446aa30915c"
auth_token = "7c0f59b1d84a06d74a56e89415987212"

weather_parameters = {
    "lat": 33.753746,
    "lon": -84.386330,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]  # slices data to retrieve first 12 hours

will_rain = False

for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today in Atlanta, remember to bring an umbrella.",

        from_='+19064482243',
        to='+16789070045'
    )

# |The code below was my initial solution that did not use list slicing|
# hour_list = weather_data["hourly"]
# creates a list of hourly information from weather data

# print(hour_list)
# shows all 48 hour stats
# for i in range(12):
# range 12 for 12-hour forecast stats
# individual_hour = hour_list[i]
# print(individual_hour)
# print(individual_hour["weather"])
# individual_hour_weather_id = individual_hour["weather"][0]["id"]
# print(individual_hour_weather_id)
# this could have been simplified to a one line by typing: weather_data["hourly"][i]["weather"][0]["id"]
