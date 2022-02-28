#option 1
import smtplib, ssl
import getpass

port = 465
password = getpass.getpass(prompt="Enter your password and press enter:")
print(password)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("kraftonbot2@gmail.com",password)