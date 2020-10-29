from twilio.rest import Client
#import twilio
import os

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    # Get credentials from the .env file
    account_sid = os.getenv("API_HOST")
    auth_token = os.getenv("API_KEY")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+17243906722',
        to=''+to
    )

    print(message.sid)
