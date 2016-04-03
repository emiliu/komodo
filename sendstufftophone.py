from twilio.rest import TwilioRestClient

account_sid = "ACe1b841114bb532eab845e83995f2ab3c"
auth_token = "29851e1d4546574268457ff09472f807"

client = TwilioRestClient(account_sid, auth_token)

contactNumber = "+18482166055"

messages = client.messages.list()

for i in messages:
	client.messages.delete_instance(i.sid)

client.messages.create(to=contactNumber, from_="+12015089231", body="Bob has completed The Catcher in the Rye. Would you like to send him a quote? Y/N")

while True:
	messages = client.messages.list()

	for i in messages:
		if i.body == "Y":
			client.messages.create(to=contactNumber, from_="+12015089231", body="Message sent.")
			break;
		elif i.body == "N":
			client.messages.create(to=contactNumber, from_="+12015089231", body="That's too bad.")
		else:
			a=1