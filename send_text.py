#!/usr/bin/env python3
import smtplib
import os
from send_email import send_email
import sys
import re


"""
Alltel                  sms.alltelwireless.com  
AT&T                    txt.att.net 
Boost Mobile            sms.myboostmobile.com   
Cricket Wireless        mms.cricketwireless.net 
MetroPCS                mymetropcs.com  
Republic Wireless       text.republicwireless.com   
Sprint                  messaging.sprintpcs.com 
T-Mobile                tmomail.net
U.S. Cellular           email.uscc.net
Verizon Wireless        vtext.com   
Virgin Mobile           vmobl.com   
""" 

complete_carrier_domains=["sms.alltelwireless.com","txt.att.net","sms.myboostmobile.com","mms.cricketwireless.net","mymetropcs.com","text.republicwireless.com","messaging.sprintpcs.com","tmomail.net","email.uscc.net","vtext.com","vmobl.com"]
carrier_domains=["tmomail.net","txt.att.net","vtext.com"]


#works on my phone ["mymetropcs.com","tmomail.net","vmobl.com"]

def send_text(numbers:[str],text:str):
    assert type(text)==str
    assert type(numbers[0])==str
    assert len(text)<160
    email_addrs=[]
    for num in numbers:
        for cd in carrier_domains:
            email_addrs.append(num+"@"+cd)
    print(email_addrs)
    send_email(email_addrs,"_",text)

def main():
    if len(sys.argv)!=3:
        print("usage:")
        print("\texport EMAIL_ADDR=<your_email@gmail.com>")
        print("\texport EMAIL_PSWD=<your email password>")
        print("\t./send_text.py <phone number> <text message>")
        print("example:")
        print("\texport EMAIL_ADDR=terrence-davis@gmail.com")
        print("\texport EMAIL_PSWD=gu3ssth1sCIA")
        print("\t./send_text.py 1123581323 'I report to God. You report to me.'")
        return
    if len(re.findall(r'[a-z0-9\-]+@gmail\.com',os.environ["EMAIL_ADDR"]))==0:
        print("error: "+os.environ["EMAIL_ADDR"]+" is not gmail")
        return
    send_text([sys.argv[1]],sys.argv[2])


if __name__ == '__main__':
    main()





















#