import smtplib
import getpass 

# Creating a SMTP connection
HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "alexisreyna01@outlook.com"
TO_EMAIL = "alexis.reynasz@uanl.edu.mx"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: Mail sent using python
                Hi, this is a test message.

                Thanks.
                From me, to me."""

smtp = smtplib.SMTP(HOST,PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()

