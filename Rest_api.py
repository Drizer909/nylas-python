pip install nylas
from nylas import APIClient

nylas = APIClient(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)
message = nylas.messages.first()
subject = message.subject

print(subject)
from nylas import APIClient

nylas = APIClient(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

# Create a new email draft.
draft = nylas.drafts.create()

# Set the recipient email address.
draft.to = ["recipient@example.com"]

# Set the email subject.
draft.subject = "This is the subject of my email."

# Set the email body.
draft.body = "This is the body of my email."

# Send the email.
draft.send()
