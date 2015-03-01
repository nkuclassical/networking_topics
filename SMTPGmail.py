import smtplib
fromaddr = 'user_name@gmail.com'
toaddrs  = 'receiver@example.com'
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: receiver@example.com",
  "Subject: SMTP Test",
  "Hello SMTP! It's an email from GMAIL SMTP"
  ])
username = fromaddr
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()