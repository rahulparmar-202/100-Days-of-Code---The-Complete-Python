

# ------------------ HOW TO SEND EMAIL - using Python ------------------


#  import smtplib
#
# my_gmail = "YOUR_EMAIL"
# password = "YOUR_PASSWORD"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_gmail, password=password)
#     connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs="RECEIVER'S_EMAIL",
#         msg="Subject:this is the subject\n\n This is the body message for email."
#     )


import datetime as dt

now  = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(day_of_week)
print(now)
print(year)

date_of_birth = dt.datetime(year=2005, month=2, day=20)