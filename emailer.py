from smtplib import SMTP # smtplib for connection and sending of email
from email.mime.text import MIMEText # MIMEText for formatting
from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender

'''
Sending an email in python useing smtplib, python default library and mime text to format message
'''

email_recipient = input('Type the recipients email: ')
email_user = input('**ONLY WORKS FOR GMAIL ACCOUNTS** Type your email: ')
email_pass = input('Type your email password: ')

subject = input('Type your email subject: ')
email_message = input('**USE \\n for new lines** Type your email message: ')

# Message formatting
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(email_message,'plain'))
message = msg.as_string()

# sending code
smtp_server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
smtp_server.ehlo_or_helo_if_needed()
smtp_server.starttls()
smtp_server.ehlo_or_helo_if_needed()
smtp_server.login(email_user, email_pass)
smtp_server.sendmail(email_user, recipient_email, message)
smtp_server.quit()
print(f'Email Sent to {email_recipient')
