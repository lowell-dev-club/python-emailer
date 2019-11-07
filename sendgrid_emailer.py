# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

htmlContent = '''
<!DOCTYPE html>
<html>
<head>
<style>
.coolclass {
  color: rgb(255, 175, 175);
}
.smallText {
  color: #ddd
  font-size: 7px;
}
</style>
</head>
<body>
<h1>Hello There.</h1>

<p class="coolclass">Welcome to my html file</p>

<p>Thanks<br>-Lowell Dev Club</p>
<p class="smallText>Sent using python!</p>
<a href="https://www.lowelldev.club/">Our website!</a>
</body>
</html>
'''

message = Mail(
    from_email='any_email_name@domain.com',
    to_emails='email_to_send_to@domain.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content=htmlContent)
try:
    sg = SendGridAPIClient(APIKEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
