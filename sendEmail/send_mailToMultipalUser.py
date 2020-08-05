import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'vedant nandi'
email['to'] = 'v.nandi14@gmail.com'
email['subject'] = 'sending msg using html script'

email.set_content(html.substitute(name = 'rahul'),'html')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('fakemail20to21','FakeMail@20To21')
    smtp.send_message(email)
    print('all good thik soooo')