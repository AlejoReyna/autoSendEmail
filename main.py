import smtplib
import getpass 

# Creating a SMTP connection
HOST = "smtp-mail.outlook.com"
PORT = 587

#JustFuckingCode!
# Data of email
FROM_EMAIL = "sender_email@email.me"
TO_EMAIL = "receiver_email@email.me"
PASSWORD = getpass.getpass("Enter password: ")

# Message
MESSAGE = """ Here goes the message """

# Connection to SMTP lib (using outlook) :)
smtp = smtplib.SMTP(HOST,PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()

