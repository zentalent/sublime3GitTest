from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

who = 'zentalent@163.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg
Hello world!
''' % {'who': who }

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who,[who],origMsg)
sendSvr.quit()
assert len(errs) == 0,errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('zentalent@163.com')
recvSvr.pass_('zen_870729')
rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody