import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
from email_addr import *

config = dotenv_values(".env")

email = EmailMessage()

email['from'] = email_from
email['to'] = email_to
email['cc'] = email_to

email['bcc'] = [mail for mail in email_bcc]

email['subject'] = 'Good Day!!'

email.set_content('Test')

with smtplib.SMTP(host=config["HOST"], \
                  port=config["PORT"]) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config['USERNAME'], config['PASSWORD'])
    smtp.send_message(email)
    print('done')