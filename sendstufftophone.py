from twilio.rest import TwilioRestClient

account_sid = "ACe1b841114bb532eab845e83995f2ab3c"
auth_token = "29851e1d4546574268457ff09472f807"

client = TwilioRestClient(account_sid, auth_token)

contactNumber = "+18482166055" 
"""+18482166055"""
targetNumber = "+17323479687"

messages = client.messages.list()

client.messages.create(to=contactNumber, from_="+12015089231", body="Maya has completed The Catcher in the Rye. Would you like to send him a quote? Y/N")

for i in messages:
	client.messages.delete_instance(i.sid)

okleave = 0

while True:
	messages = client.messages.list()

	for i in messages:
		if i.body == "Y":
			client.messages.create(to=contactNumber, from_="+12015089231", body="Message sent.")
			client.messages.create(to=targetNumber, from_="+12015089231", body="Insert Inspirational Quote")
			okleave = 1
		elif i.body == "N":
			client.messages.create(to=contactNumber, from_="+12015089231", body="That's too bad.")
			okleave = 1
		else:
			a=1

	if (okleave == 1):
		break;