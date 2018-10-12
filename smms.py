import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("rosethasin@gmail.com", "bankrobber") 
  
# message to be sent 
message = "hellloooooo"
  
# sending the mail 
s.sendmail("rosethasin@gmail.com", "nagendrasr02@gmail.com", message) 
  
# terminating the session 
s.quit() 