from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import binascii
import datetime
import fcntl
import hashlib
import math
import smtplib
import socket
import struct
import time
import traceback
import urllib

recipient = ""

GMAIL_USER = u''
GMAIL_PASS = u''
SMTP_SERVER = u'smtp.office365.com'
SMTP_PORT = 587
  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
subject =s.getsockname()[0]

def send_ip(recipient, subject, text):
  print("Mail to "+recipient+" about "+subject+" : "+text)
  try:
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = u'To:' + recipient + u'\n' + u'From: ' + GMAIL_USER
    header = header + '\n' + u'Subject:' + subject + u'\n'

    msg = MIMEMultipart('alternative')
    msg.set_charset('utf8')
    msg['From'] = GMAIL_USER
    msg['To'] = recipient
    msg['Subject'] = Header(
        subject.encode('utf-8'),
        'UTF-8'
    ).encode()

    _attach = MIMEText(text.encode('utf-8'), 'plain', 'UTF-8')
    msg.attach(_attach)
    print(msg.as_string())

    smtpserver.sendmail(GMAIL_USER, recipient, msg.as_string())
    smtpserver.close()
    print("DONE")
    return True
  except:
    traceback.print_exc()
    return False


send_ip(recipient, subject, subject)
