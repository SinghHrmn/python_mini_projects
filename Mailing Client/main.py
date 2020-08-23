import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

sever.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

email = "youremail@provider.com"

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'Harmandeep Singh'
msg['To'] = 'recievermail@gmail.com'
msg['Subject'] = 'Just a Test'