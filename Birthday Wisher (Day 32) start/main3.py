import pandas
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = "dcomputer023@gmail.com"
MY_PASSWORD = "rtpo kswj cqta sojp"

data = pandas.read_csv("birthdays.csv")
data_row = data[data.name == "Zainab"]

now = dt.datetime.now()
today = (now.month, now.day)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    birthday_person = birthday_dict[today]
    with open(file_path) as letter_file:
        letter_content = letter_file.read()
        letter_content.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Birthday Message\n\n{letter_content}")
