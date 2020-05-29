import smtplib, ssl
import getpass
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "mandal.a.2607@gmail.com"
receiver_email = "srock350sd@gmail.com"
password =getpass.getpass('enter pass ->')
message = "Model training failed"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
