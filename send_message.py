from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid ="AC076ff0a02132e85ab96e0df0b7d6cc9b"
# Your Auth Token from twilio.com/console
auth_token  = "fc8d59eaa1c99d92524e9c4f262ff9b6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886958890166",
    from_="+12053465525",
    body="Hello from Python!")

print(message.sid)
