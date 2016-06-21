#Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


def send_sms():
	#Login credentials for the API
	username = "alexmagana"
	apikey = "7854c8cccb76f963613888d2584f60bd265607bd8d2d1c3cb7a0c1e8ddd50aa1"
	
	#The recipient(s) of the message
	to = "+254729071228,+254702212525"
	
	#The details of the sender
	#sender = "ALEX MAGANA"
	
	#The content of the message to send to be sent
	message = "This is a test, I hope you've been able to locate an M-Pesa agent."
	
	#Create an instance of the AfricasTalkingGateway class
	gateway = AfricasTalkingGateway(username, apikey)
	
	#Wrap the API call in a try-catch block, to capture any gateway errors that may arise
	try:
		#Call sendMessage function
		results = gateway.sendMessage(to,message)
		#results = gateway.sendMessage(to,message, sender)
		
		for recipient in results:
			#Evaluate the status response
			#The function returns "Success" or "error-message"
			print "number=%s;status=%s;messageId=%s;cost=%s" % (recipient['number'],
																recipient['status'],
																recipient['messageId'],
																recipient['cost'])
	except AfricasTalkingGatewayException, e:
		print "Encountered an error while sending: %s" % str(e)