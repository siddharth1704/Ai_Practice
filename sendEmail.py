import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address='sid17singh@gmail.com';
    password = getpass.getpass()  # to input paswword without displaying anything
    subject='Testing Email Service'
    msg='''
     This is a bot generated email kindly do not reply
     Thank you
     Sid'''
    #server intialization
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)
    recipents = ['sid1724@yahoo.com', 'mridulrao674385@gmail.com']
    #draft my message
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']=",".join(recipents)

    server.sendmail(sender_address,recipents,msg.as_string())

send_email()