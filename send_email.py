import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "garar9774@gmail.com"
password = "rhbw psea vzve jzvt"
receiver_email = "lateefayodele123@gmail.com" # replace with the Gmail App Password (not your normal password)

# Email content
subject = "Automated Message"
body = "Hello! This is an automated message sent from my Python script."

# Build the email
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.set_debuglevel(1)
    server.login(sender_email, password)
    server.send_message(msg)

print("✅ Email sent successfully!")
