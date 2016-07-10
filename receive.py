# coding:utf-8

import imaplib, re
import email

from email import Utils
from email.header import decode_header
user = "mhotmoney96@gmail.com"
password = "indezamoney55"
label = "INBOX"

gmail = imaplib.IMAP4_SSL("imap.gmail.com")

#ログイン
gmail.login(user, password)

#ラベル一覧
gmail.list()

#ラベル選択
gmail.select(label)

#未読一覧
typ, [data] = gmail.search(None, "UNSEEN")

result, data = gmail.fetch(data, "(BODY[TEXT])")
raw_email = data[0][1]
msg = email.message_from_string(raw_email)
msg_subject = decode_header(msg.get('Subject'))[0][0]
print msg_subject.get_payload().decode('iso-2022-jp')
#print data,'iso-2022-jp'
#bodytxt = str(data[0][1], 'iso-2022-jp', 'replace')

'''
for num in data.split():

    result, data = gmail.fetch(num, "(BODY[TEXT])")

    #エンコード
    bodytxt = str(data[0][1], 'iso-2022-jp', 'replace')

    #空文字で分割
    r=re.compile(r'^\s*', re.M)

    #文字抽出
    kiji= [i for i in r.split(bodytxt) if '不審者の出没事案<今治署管内>' in i]

    if kiji:
        for i in kiji:
            print(i)

    #メール既読
    gmail.store(num, "+FLAGS", r"\SEEN")
'''
gmail.close()
gmail.logout()