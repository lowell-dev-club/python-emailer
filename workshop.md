# Python Emailer

using an online [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) **[REPL.it](https://repl.it)**

## API

What is an API?  

An API (Application programming interface) is a computer science term describing something a program uses to interact with another programming service, for example, informational services like dictionaries, or connecting and using servers.  

[Read more about APIs!](https://en.wikipedia.org/wiki/Application_programming_interface)  

Today's workshop uses an API created by [Twilio](https://www.twilio.com/) called Send Grid. It uses an API key to allow access for a user to send an email. It takes inputs for who your sending to, who is sending (doesn't have to be an email), the subject, an html body.

## Repl.it

Create a new repl and choose python. Make sure its specified as Python or Python 3. **Do Not Use Python 2**

![repl it image](https://github.com/lowell-dev-club/python-text-game/blob/master/replit.png?raw=true)

## Creating the program

#### Imports

We start by importing the needed code from the sendgrid library.

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
```

#### Configuring the email

Input all the values needed for sending the email and with the messages you want.

```python
message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
```
#### Completeing the code

We will display and give out an API key to use for your program.  
We use try and except to catch possible errors when sending your email.

```python
try:
    sg = SendGridAPIClient(APIKEY))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```

View the code file [here](emailer.py)  
