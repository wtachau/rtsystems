# Import smtplib for the actual sending function
import smtplib
import sys

# Import the email modules we'll need
from email.mime.text import MIMEText

def send_email(data):

	sys.stdout.flush()

	gmail_user = "rtsystemsbot@gmail.com"
	gmail_pwd = "xr1WG5Nk"
	FROM = 'rtsystemsbot@gmail.com'
	TO = ['will@rtsystems.io', 'james@rtsystems.io']
	SUBJECT = "rtsystems.io contact form submission, ya bish"
	TEXT = "Dis bish named %s (phone # %s) at %s said this: '%s'" % (data['name'], data['phone'], data['email'], data['comments'])

	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		#server = smtplib.SMTP(SERVER) 
		server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		#server.quit()
		server.close()
		print 'successfully sent the mail'
	except:
		print "failed to send mail"