from smtplib import SMTP # smtplib for connection and sending of email
from email.mime.text import MIMEText # MIMEText for formatting
from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender

'''
Sending an email in python useing smtplib, python default library and mime text to format message
'''

email_recipient = email_recipient
pass_path = pass_path
email_user = data['email_address'] # get email address
email_pass = data['email_password'] # get email password
# message area
msg = MIMEMultipart() # formatting
msg['From'] = email_user
msg['To'] = recipient_email # input recipient email
msg['Subject'] = subject # input subject
msg.attach(MIMEText(email_message,'plain')) # add body
message = msg.as_string() # format all text

# sending code
smtp_server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
smtp_server.ehlo_or_helo_if_needed()
smtp_server.starttls() #start connection
smtp_server.ehlo_or_helo_if_needed()
smtp_server.login(email_user, email_pass) # login with credentials
smtp_server.sendmail(email_user, recipient_email, message) # send email
smtp_server.quit() # quit connection
print('Email Sent!') # done
