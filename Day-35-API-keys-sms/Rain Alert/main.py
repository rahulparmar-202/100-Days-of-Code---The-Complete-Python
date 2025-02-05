import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
# this loads the environment variables from the .env file

# my twilio phone_number = +18314804850
account_sid = "AC5473d59d7ebbac0eb90aa96530ed506c"
auth_token = os.getenv("AUTH_TOKEN")

# api endpoint syntax :
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=api_key


api_key = os.getenv("OWM_API_KEY")
# This api gives 5-Days weather data and in every 3-Hours.
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 24.922569,
    "lon": 72.684761,
    "appid": api_key,
}
# "cnt":4  = can add this to the weather_params to get only next 12 hours data

# 40.440624,  -79.995888  > Pittsburgh - for example
"""
My Lat-long = 
# "lat" = 24.922569
# "lon" = 72.684761
"""

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(f"Status:{response.status_code}")


will_rain = False
# weather_data["list"][:4] = will take only first 4 data that is of 12 hours
hour_data = [item["weather"][0]["id"] for item in weather_data["list"][:4]]
for condition_code in hour_data:
    if int(condition_code)< 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    # sends the message to the whatsApp number
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Hey Rahul \nIt's going to rain ⛈️ today, Don't forget your Umbrella.☔️",
        to='whatsapp:+916367906870'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Hi Rahul \nIt's going to be a Sunny Day Today. ☀️",
        to='whatsapp:+916367906870'
    )
    print(message.status)



# -------- IMP --> Environment Variables -------------- #
"""
🌍 What Are Environment Variables?
Environment variables are key-value pairs stored in your operating system that can be accessed by programs. They help keep sensitive data (API keys, passwords, etc.) secure by not hardcoding them in your code.

📌 Why Use Environment Variables?
✅ Security – Protects sensitive data (API keys, database passwords).
✅ Flexibility – Easily change settings without modifying the code.
✅ Portability – Works across different machines and cloud services.
"""