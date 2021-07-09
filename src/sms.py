from twilio.rest import Client
import os

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.getenv("sid")
    auth_token = os.getenv("token")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+12013899753',
        to='+19546465110'
    )

    print(message.sid)

    