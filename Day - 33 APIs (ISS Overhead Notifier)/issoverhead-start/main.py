import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()
# this loads the environment variables from the .env file

# ISS : International Space Station

MY_LAT = 24.922569 # Your latitude:
MY_LONG = 72.684761  # Your longitude:

MY_EMAIL = os.getenv("MY_GMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


# this function compares the iss lat-long to my lat-long and returns True-False
def iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    # raise exceptions if the there are any
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.

    # if iss_latitude in range(int(MY_LAT - 5), int(MY_LAT + 5)) and  iss_longitude in range(int(MY_LONG - 5), int(MY_LONG + 5)):
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


# function that returns if it is night or day still
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # split the sunrise and sunset time to hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

# this function sends the mail
def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=os.getenv("RECEIVER_EMAIL"),
            msg="Subject:ISS info\n\nLOOK UP , The ISS is hovering over you."
        )
        print("Mail Sent!")


# runs every 60 seconds
while True:
    # sleep 60 sec then run again
    time.sleep(60)
    if iss_overhead and is_night:
        send_mail()
    else:
        print("The ISS is not around your location.")



# Steps :-
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




