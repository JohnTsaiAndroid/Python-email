#-*- coding: utf-8 -*-
from email.mime.text import MIMEText
import time
#timestr=time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
#msg = MIMEText('hello, Nice to meet you send by Python...\n'+timestr, 'plain', 'utf-8')
# ����Email��ַ�Ϳ���:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# ����SMTP��������ַ:
smtp_server = raw_input('SMTP server: ')
# �����ռ��˵�ַ:
to_addr = raw_input('To: ')


import smtplib
import time
server = smtplib.SMTP(smtp_server,25) # SMTPЭ��Ĭ�϶˿���25
server.set_debuglevel(1)
server.login(from_addr, password)
for i in range(100):
    time.sleep(1)	
    timestr=time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
    msg = MIMEText('hello, Nice to meet you send by Python...\n'+timestr, 'plain', 'utf-8')
    server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()