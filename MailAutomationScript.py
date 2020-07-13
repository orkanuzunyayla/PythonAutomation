import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders


n=0
with open('mails.txt') as mails: #create a .txt file to your working directory with the list of emails which you want to send the mail to.
    email_send = mails.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
email_send = [x.strip() for x in email_send]

# sender email address
email_user = 'Your Email'
# sender email passowrd for login purposes
email_password = 'Your EMail Password' #Some email service providers like Google may require you to enable external apps to access your mail.
subject = 'Your Subject'
msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = subject

path_to_pdf = 'Path to the pdf you want to attach' #Relative path to your current working directory
with open(path_to_pdf, "rb") as f:
	#attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
	attach = MIMEApplication(f.read(),_subtype="pdf")
	attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))

body = """Email Body
Multi Line is Ok.
"""
msg.attach(MIMEText(body,"plain"))
msg.attach(attach)
text = msg.as_string()

for elements in email_send:
	currentEmail = email_send[n]
	msg['To'] = currentEmail
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)
	server.sendmail(email_user,currentEmail,text)
	n=n+1
	print(currentEmail)
	msg['To'] == None
	server.quit()