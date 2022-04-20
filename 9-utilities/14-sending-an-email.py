import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import password
message=MIMEMultipart()
message["from"]="Zartab Nakhwa"
message["to"]="nzartab@gmail.com"
message["subject"]="Mail from Intuit Python Batch"

body="Hey, this is a test message"

message.attach(MIMEText(body))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("codewithz21@gmail.com",password.get_password())
    smtp.send_message(message)
    print("Sent.....")