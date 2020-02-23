# from your Gmail account
#--------------------------------------------------------------------------------
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os
mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''

#Setup the MIME
message = MIMEMultipart()

message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail

attach_file_name = 'image.jpg'
attach_file = open(attach_file_name, 'rb').read() # Open the file as binary mode

image = MIMEImage(attach_file,name=os.path.basename(attach_file_name))
message.attach(image)
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login('sender mail id', 'sender password') #login with mail_id and password
text = message.as_string()
session.sendmail('sender mail id', 'receiver mail id', text)
session.quit()
