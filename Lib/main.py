import requests
import smtplib
import os
from datetime import datetime

MY_EMAIL = "jrydel92@gmail.com"
MY_PW = os.environ.get("G_SMTP_PW")
def sunrise_email():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PW)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,
                                msg="Subject: Sunrise\n\nThe sun has arisen.")
def sunset_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PW)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject: Sunset\n\nThe sun has descended.")


now = datetime.now()

api_request = "https://api.sunrise-sunset.org/json?formatted=0"

response = requests.get(api_request, timeout=60)
jdata = response.json()
response.raise_for_status()

sunrise_hour = jdata["results"]["sunrise"].split("T")[1].split(":")[0]
sunrise_min = jdata["results"]["sunrise"].split("T")[1].split(":")[1]

sunset_hour = jdata["results"]["sunset"].split("T")[1].split(":")[0]
sunset_min = jdata["results"]["sunset"].split("T")[1].split(":")[1]

if now.hour == sunrise_hour and now.min == sunrise_min:
    sunrise_email()

if now.hour == sunset_hour and now.min == sunset_min:
    sunset_email()
