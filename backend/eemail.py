import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
email_address = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

msg = EmailMessage()
msg["Subject"] = "test"
msg["From"] = email_address
msg["To"] = email_address
msg.set_content("Hello, \n Testiiing!!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
   smtp.login(email_address,password)
   smtp.send_message(msg)

print(msg.get_content())

