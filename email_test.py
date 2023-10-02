import os
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values

config = dotenv_values(".env")

email = EmailMessage()
email['from'] = 'mustafa.prodhan2@gmail.com'
email['to'] = 'mustafizur.prodhan@gmail.com'
email['subject'] = 'Test'

email.set_content('Test')

with smtplib.SMTP(host=config["HOST"], \
                  port=config["PORT"]) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config['USERNAME'], config['PASSWORD'])
    smtp.send_message(email)
    print('done')