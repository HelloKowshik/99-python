import smtplib

sender = 'usr@bd.com'
receiver = 'user1@bd.com'
password = '12345'
subject = 'Test Mail in Python'
body = 'Hello World!'

message = f"""From: {sender}
To: {receiver}
Subject: {subject}
{body}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    print('OK')
    server.sendmail(sender, receiver, message)
    print('Mail Sent...')
except smtplib.SMTPAuthenticationError as e:
    print(e)
