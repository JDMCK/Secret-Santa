import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import date

class Santa:
    def __init__(self, name, email, child):
        self.name = name
        self.email = email
        self.child = child

Jesse = Santa('Jesse', 'jesse@jessemckenzie.com', 'UA')
Cara = Santa('Cara', 'cara@gmail.com', 'UA')
Steve = Santa('Steve', 'steve@gmail.com', 'UA')
Josh = Santa('Josh', 'josh@gmail.com', 'UA')
Evan = Santa('Evan', 'evan@gmail.com', 'UA')

# Email credentials
email_address = "secretsantaport@gmail.com"
email_password = "PASSWORD"

# SMTP server configuration
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
smtp_port = 587  # Usually 587 for TLS or 465 for SSL

# Recipients list
recipients = [Jesse, Josh, Evan, Steve, Cara]

# Special handling
flag = True
while flag:
    flag = False
    random.shuffle(recipients)
    for i in range(len(recipients)):
        if (recipients[i].name == 'Steve' and recipients[i - 1] == 'Cara') or (recipients[i].name == 'Cara' and recipients[i - 1] == 'Steve'):
            flag = True


for i in range(len(recipients)):
    recipients[i].child = recipients[i-1]

# SaveLog People

f = open('SaveLog.txt', 'a')

f.write(date.isoformat(date.today()) + ' ' + time.strftime('%H:%M:%S', time.localtime()) + '\n')
for i in recipients:
    f.write('{} -> {}\n'.format(i.name, i.child.name))
f.write('\n')

# Email content
subject = "SECRET SANTA 2023!"

# Create the email
message = MIMEMultipart()
message["From"] = email_address
message["Subject"] = subject

# Send the email to each recipient
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(email_address, email_password)

        for santa in recipients:
            msg = message.as_string()
            message["To"] = santa.email
            body = """
            Hello {}!
            Welcome to Secret Santa 2023, I hope you are as excited as I am!
            I am a bot that is in charge of assigning who everyone is paired with to ensure that nobody knows who has who!
            This process was done completely randomly and SECRETLY!

            The person you will be buying a gift to is...

            {}!!!

            The spending limit for this gift is 100CAD, a drop in the bucket for some people!

            Have fun and thank you for participating in this years Secret Santa!
            """.format(santa.name, santa.child.name, santa.child.name, santa.child.address)

            message.attach(MIMEText(body, "plain"))

            server.sendmail(email_address, santa.email, msg)
            print(f"Email sent to {santa.name}")




    print("All emails sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
