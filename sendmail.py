import smtplib, ssl`

SENDER_EMAIL = 'gomesjoshua42@gmail.com'
SENDER_PASSWORD = 'Qwert123!'

def sendmail(receiver_email, subject, body):
    message = (f'Subject: {subject}n\n{body}')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)
