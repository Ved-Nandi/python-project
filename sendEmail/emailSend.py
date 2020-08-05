import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'user'
email['to'] = 'akshaysatpute2016@gmail.com'
email['subject'] = 'hack'

email.set_content('subject is not important')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('fakemail20to21','FakeMail@20To21')
    smtp.send_message(email)
    print('all good thik soooo')