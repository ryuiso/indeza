#!/usr/bin/env python
# -*- coding: utf-8 -*-

# send mail utf-8 using gmail smtp server /w jpegs

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from email.Header import Header
from email.Utils import formatdate
import smtplib

import cv2
def send_email_with_jpeg(from_addr, to_addr, subject, body, jpegs=[], server='smtp.gmail.com', port=587):
    encoding='utf-8'
    msg = MIMEMultipart()
    mt = MIMEText(body.encode(encoding), 'plain', encoding)

    if jpegs:
        for fn in jpegs:
            img = open(fn, 'rb').read()
            mj = MIMEImage(img, 'jpeg', filename=fn)
            mj.add_header("Content-Disposition", "attachment", filename=fn)
            msg.attach(mj)
        msg.attach(mt)
    else:
        msg = mt

    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    _user = "mhotmoney96@gmail.com"
    _pass = "indezamoney55"

    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(_user, _pass)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())
    smtp.close()

###
if __name__ == '__main__':
    body = u'\n%s\n    --- %s\n' % (u'お祝いありがとう！', u'これ買ったよ！')
    #js = ['jobs0.jpeg', 'jobs.jpeg']
    js = ['sample.jpg']
    send_email_with_jpeg('mhotmoney96@gmail.com', 'mhotmoney96@gmail.com', u'プレゼントの感謝メール', body, js)