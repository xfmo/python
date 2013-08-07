#!/usr/bin/env python
#-*-coding:utf-8-*-
import poplib,email
from email.header import decode_header
from email.mime.text import MIMEText
from email import parser
import smtplib
import time
import os, sys
import random


def accp_email():
    """
    
    """
    try:
        pop = poplib.POP3('pop.qq.com')
        pop.user('906539210')
        pop.pass_('Icanmakeit1107')
    except poplib.error_proto, e:
        print e
        return 1
    for item in pop.list()[1]:
        number, octets = item.split(' ')
        lines = pop.retr(number)[1]
        msg = email.message_from_string('\n'.join(lines))
        print "$$$"*10
        print number
        print msg.get_payload(),dir(msg.get_payload())
        print "=========="*5


def send_email(content,sub='电脑发送',to='906539210@qq.com', user='2008124025@163.com',pwd='031188557891'):

    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = user+"<"+user+">"
    msg['To'] = to
    try:
        handle = smtplib.SMTP('smtp.163.com',25)
        handle.login(user,pwd)

        handle.sendmail(user,to,msg.as_string())
        handle.close()
        print 'ok'
        return 1
    except Exception, e:
        print 'error',e
        return 0


if __name__ == "__main__":
    #accp_email()
    send_email('ok !')
