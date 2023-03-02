import smtplib
from email.mime.text import MIMEText
import pw
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
subject = "发给老王的一封邮件"
body = "Hello world"
sender = "laowangdr@gmail.com"
recipients = ["laowangdr@gmail.com"]
password = pw.email_pw
send_email(subject, body, sender, recipients, password)
