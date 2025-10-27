import smtplib

sender_mail="example.outlook.com"
sender_password="qesDoheuodJIJ"

def sent_email(receiver_mail,subject,body):
    message=f"Subject:  {subject}\n\n {body}"
    with smtplib.SMTP("smtp.office365.com",587) as server:
        server.starttls()
        server.login(sender_mail,sender_password)
        server.sendmail(sender_mail,receiver_mail,message)

sent_email("example2.gmail.com","looking for update","hello ....")

'''

This script sends an email automatically using SMTP (Simple Mail Transfer Protocol) — helpful for notifications, updates, etc.

🔹 1. Imports
import smtplib


Imports the SMTP library, used to connect to mail servers and send emails.

🔹 2. Email Credentials
sender_mail = "example.outlook.com"
sender_password = "qesDoheuodJIJ"


These store the sender’s email ID and password (or app password).

⚠️ Important: Never hard-code passwords — use environment variables instead.

🔹 3. sent_email(receiver_mail, subject, body) Function

What it does: Sends an email with a given subject and message to the receiver.

How it works:

Creates the email format:

message = f"Subject: {subject}\n\n{body}"


Connects to the Outlook SMTP server:

smtplib.SMTP("smtb.office365.com", 587)


587 → port for TLS encryption.

starttls() → secures the connection.

Logs in and sends the email:

server.login(sender_mail, sender_password)
server.sendmail(sender_mail, receiver_mail, message)

🔹 4. Example Call
sent_email("example2.gmail.com", "looking for update", "hello ....")


Sends an email:

To: example2@gmail.com

Subject: looking for update

Body: hello ....

⚙️ 5. Key Takeaways

✅ smtplib lets you send emails easily from Python.
✅ Always use secure ports and TLS (starttls()).
✅ Never expose passwords in code.
✅ You can use Gmail, Outlook, Yahoo, etc., with their respective SMTP servers.
'''