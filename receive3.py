# -*- coding: UTF-8 -*-

import imaplib

from email.header import decode_header



gmail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

gmail.login('mhotmoney96@gmail.com', 'indezamoney55')


# 受信トレイを選択

gmail.select('INBOX')



# 未読のカウント

status, response = gmail.status('INBOX', "(UNSEEN)")

unreadcount = int(response[0].split()[2].strip(').,]'))

print unreadcount

# 受信トレイから、１つめのメールを取り出してみる。

status, count = gmail.select('Inbox')

status, count = gmail.select()

last_mail_id = int(count[0])
print "last_mail:" + str(last_mail_id)

#status, data = gmail.fetch(count[0], '(UID BODY[TEXT])')
status, data = gmail.fetch(last_mail_id, '(UID BODY[TEXT])')

#print "status:"+str(status)
#print "data:"+str(data[0][1])
_,[data] = gmail.search(None,'ALL')
for i in data.split(' '):
    _,sub = gmail.fetch(i,'(BODY[HEADER.FIELDS (SUBJECT)])')

decoded = decode_header(sub[0][1].strip())

print decoded


text =unicode(decoded)
print text
#print unicode(decoded[0], decoded[1])

'''
print "body:"+unicode(decoded[0], decoded[1])
print "data:"+str(data[0][1])
'''
'''
print data[0][1]

# デコードしないとだめだね



# サブジェクトを表示してみる

_,[data] = gmail.search(None,'ALL')

for i in data.split(' '):

    _,sub = gmail.fetch(i,'(BODY[HEADER.FIELDS (SUBJECT)])')

    # デコードして表示してみようか

    decoded = decode_header(sub[0][1].strip())[1]

    print len(decoded)

    print "body:"+unicode(decoded[0], decoded[1])

'''

gmail.close()

gmail.logout()