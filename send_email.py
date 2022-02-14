#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import sys
import os
import re


def send_email(receivers:[str],subject:str,text:str,filename:str=""):
    assert type(subject)==str
    assert type(text)==str
    assert type(receivers[0])==str
    assert type(filename)==str
    msg=EmailMessage()
    msg['Subject']=subject
    msg['from']=os.environ["EMAIL_ADDR"]
    msg['To']=receivers
    msg.set_content(text)
    if filename!="":
        with open(filename,"rb") as fd:
            data=fd.read()
            fn=filename.split("/")[-1]
            msg.add_attachment(data,filename=fn,maintype='image',subtype='')

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        sender=os.environ["EMAIL_ADDR"]
        smtp.login(sender,os.environ["EMAIL_PSWD"])
        # msg="Subject: "+subject+" \n\n"+text
        # smtp.sendmail(sender,receivers,msg)
        smtp.send_message(msg)

def usage():
    print("usage:")
    print("\texport EMAIL_ADDR=<your_email@gmail.com>")
    print("\texport EMAIL_PSWD=<your email password>")
    print("\t./send_email.py <recepiant email> <subject> <message>")
    print("example:")
    print("\texport EMAIL_ADDR=terrence-davis@gmail.com")
    print("\texport EMAIL_PSWD=gu3ssth1sCIA")
    print("\t./send_email.py torvalds@osdl.org '_' 'I report to God. You report to me.'")

def main():
    filename=""
    if len(sys.argv)<4 or len(sys.argv)>5:
        usage()
        return
    if len(sys.argv)==5:
        filename=sys.argv[4]
    if len(re.findall(r'[a-z0-9\-]+@gmail\.com',os.environ["EMAIL_ADDR"]))==0:
        print("error: "+os.environ["EMAIL_ADDR"]+" is not gmail")
        return
    send_email([sys.argv[1]],sys.argv[2],sys.argv[3],filename)


if __name__ == '__main__':
    main()