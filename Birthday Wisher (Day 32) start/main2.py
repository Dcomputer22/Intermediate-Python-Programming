# import smtplib
#
# my_email = "dcomputer023@gmail.com"
# password = "rtpo kswj cqta sojp"
#
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="fatimaoyiza18@gmail.com",
#                         msg="Subject:Greetings\n\nHi there! This is my content."
#                         )

import datetime as dt
from random import choice
import smtplib
#
# now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)
# if year == 2023:
#     print("Always wash your hands!")
# day_of_week = now.weekday()
# #Computers start counting from 0
# print(day_of_week)
#
# date_of_graduation = dt.datetime(year=2023, month=2, day=20)
# print(date_of_graduation)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    with open(file="quotes.txt", mode="r") as quotes_file:
        quotes_data = quotes_file.readlines()
        random_quote = choice(quotes_data)

    my_email = "dcomputer023@gmail.com"
    password = "rtpo kswj cqta sojp"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="fatimaoyiza18@gmail.com",
                            msg=f"Subject:Weekly Quotes\n\n{random_quote}")
