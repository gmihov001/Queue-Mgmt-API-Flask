from twilio.rest import Client
import os

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.getenv("sid")
    auth_token = os.getenv("token")
    sender = os.getenv("from_")
    recepient = os.getenv("to")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=sender,
        to=recepient
    )

    print(message.sid)

    