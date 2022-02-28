import csv, smtplib, ssl,datetime,time 


from_address = "kraftonbot2@gmail.com"
password = input("Type your password and press enter: ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("mails.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, dateofbirth in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,dateofbirth=dateofbirth),
            )

today = datetime.datetime.now().strftime("%d-%m")
if(today==dateofbirth):
    message = """Subject: Wishing you Happy birthday from Saif Rahman

    Hi {name}, many many happy returns of the day"""

