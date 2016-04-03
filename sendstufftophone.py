from twilio.rest import TwilioRestClient

account_sid = "ACe1b841114bb532eab845e83995f2ab3c"
auth_token = "29851e1d4546574268457ff09472f807"

client = TwilioRestClient(account_sid, auth_token)

client.messages.create(to="+18482310390", from_="+12015089231", body="asdflkjasdlfkjasdlkfjaslkdfjalksdfj")

messages = client.messages.list()

while True:
	input()

	messages = client.messages.list()

	for i in messages:
		print (i.body)

	for i in messages:
		client.messages.delete_instance(i.sid)