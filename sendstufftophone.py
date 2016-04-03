from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = "ACe1b841114bb532eab845e83995f2ab3c"
auth_token = "29851e1d4546574268457ff09472f807"

client = TwilioRestClient(account_sid, auth_token)

contactNumber = "+18482310390" 
"""+18482166055"""
targetNumber = "+17323479687"

messages = client.messages.list()

client.messages.create(to=contactNumber, from_="+12015089231", body="Maya has completed The Catcher in the Rye. Would you like to send him a quote? Y/N")

resp = twilio.twiml.Response()
resp.message('testing')