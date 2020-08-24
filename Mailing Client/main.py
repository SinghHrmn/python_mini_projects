import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message , 'plain'))

filename = 'imagename.jpg'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.send_mail('sender_mail@xyz', 'reciever_mail@xyz', text)
