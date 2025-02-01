
import requests
from datetime import datetime

MY_LAT = 24.917967
MY_LONG = 72.6875
MY_TMZ = "Asia/Kolkata"

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "tzid":MY_TMZ,
    "formatted":0
}


# we can also use this as url instead of params.
# "https://api.sunrise-sunset.org/json?lat=24.917967&lng=72.6875&tzid=Asia/Kolkata"

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_time = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset_time = data["results"]["sunset"].split('T')[1].split(':')[0]

time_now = datetime.now()
print(time_now)

print(f"Sunrise : {sunrise_time}")
print(f"Sunset : {sunset_time}")