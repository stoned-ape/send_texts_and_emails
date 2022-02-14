# Send an Email

This program connects to gmail using your gmail account and sends an email
that includes a subject, body, and optional file to attach.

For this to work, you must enable less secure apps

https://myaccount.google.com/lesssecureapps

### usage:
```bash
export EMAIL_ADDR=<your_email@gmail.com>
export EMAIL_PSWD=<your email password>
./send_email.py <recepiant email> <subject> <message> <attached file>?
```

### example:
```bash
export EMAIL_ADDR=terrence-davis@gmail.com
export EMAIL_PSWD=gu3ssth1sCIA
./send_email.py torvalds@osdl.org '_' 'I report to God. You report to me.' templeos.img
```

# Send A Text

Sending a text programmatically is as simple as sending an email
thanks to sms-gateways.

### usage:
```bash
export EMAIL_ADDR=<your_email@gmail.com>
export EMAIL_PSWD=<your email password>
./send_text.py <phone number> <text message>
```
### example:
```bash
export EMAIL_ADDR=terrence-davis@gmail.com
export EMAIL_PSWD=gu3ssth1sCIA
./send_text.py 1123581323 'I report to God. You report to me.'
```