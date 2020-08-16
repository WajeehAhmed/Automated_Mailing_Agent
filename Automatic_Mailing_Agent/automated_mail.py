import smtplib,ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) 
server.ehlo()
sender = input("Sender Email  : \n")
reciever = input("Reciever Email : \n")
server.login(str(sender),'********') #sender_email and password

msg = MIMEMultipart()
msg['From'] =  str(sender)
msg['To'] = str(reciever)
msg['Subject'] = 'Testing my automated mailing agent!'

with open('message.txt','r') as m:
    message = m.read()

msg.attach(MIMEText(message,'plain'))

file_attach = 'encoded.png'
attachment = open(file_attach,'rb')
p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={file_attach}')
msg.attach(p)
text = msg.as_string()
server.sendmail(str(sender),str(reciever),text)
server.quit()