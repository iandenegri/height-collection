from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height):
    from_email='ian.denegri@gmail.com'
    from_password='****'
    to_email=email

    subject='Average Height Data'
    message='Hey there, your height is <strong>%s</strong>. <br>Average height is %s. <br>So far there have been <strong>%s</strong> users that have submitted their height. <br> thanks for your participation.' % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
