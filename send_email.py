import smtplib

SENDER_EMAIL = 'born2codetech@gmail.com'
SENDER_PASSWORD = ''

def send_email(receiver_email, subject, body):
    message = (f'Subject: {subject}n\n{body}')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

def main():
    sub = 'This is a test email to check if it works. AAAAAND IT WORKED!!!!'
    body = 'IT WORKED'
    rec = 'gomesjoshua@gmail.com'
    send_email(rec, sub, body)

if __name__ == '__main__':
    main()
