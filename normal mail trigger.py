import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('sender mail id','sender password')
message = 'Mail sent'

s.sendmail('sender mail id','receiver mail id',message)
s.quit()
