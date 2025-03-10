# --------------------- MONDAY MOTIVATIONAL QUOTES WITH E-MAIL -------------------------

import os
import smtplib
import datetime as dt
import random

# my mail id and password
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

# gets the today data like - year-month-date, time
today = dt.datetime.today()
# get what day of the week is today :- in list index format- 0,1,2,3,4,5,6
day_today = today.weekday()
# checks if today is monday or not
if day_today == 0:
    # reading the quotes.txt that contains the quotes
    with open("quotes.txt", "r") as data_file:
        data = data_file.readlines()
        # get a quote randomly from the data (list)
        quote = random.choice(data)
    print(quote)

    # create a connection with email provider
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() # start the connection
        connection.login(user=MY_EMAIL, password=PASSWORD) # login credentials
        # sends the mail from sender_address to receiver's address, with message and mail Subject
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=os.environ.get("RECEIVER_ADRR"),
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
    print("Monday Motivational Quote Sent!")
else:
    print("Today is not Monday.")