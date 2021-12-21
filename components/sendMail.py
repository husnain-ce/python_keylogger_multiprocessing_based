from email.mime.multipart import *
from email.mime.text import *
from email.mime.base import *
from email import encoders
import smtplib, os


class SendMail:
    def __init__(self):
        self.filename = "CV"
        self.attachment = os.getcwd() + "\\" + "CV.7z"
        self.mail = "mail@gmail.com"

    def send_mail(self):
        fromaddr = self.mail
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = self.mail
        
        msg['Subject'] = "Apply for CV"
        body = "Let work for long term and I am here for working hard and smart vision " 

        msg.attach(MIMEText (body , 'plain'))

        filename =self.filename
        attachment = open(self.attachment , 'rb')

        mimebase = MIMEBase ('application' , 'octet-stream')
        mimebase.set_payload(attachment.read())
        encoders.encode_base64(mimebase)

        mimebase.add_header('Content-Disposition',"attachment;filename = %s" % filename)
        msg.attach(mimebase)
        s = smtplib.SMTP('smtp.gmail.com',587)
        
        s.starttls()
        s.login(fromaddr ,"YoursPassword")
        text = msg.as_string()
        s.sendmail(fromaddr , self.mail , text)
        s.quit()
        
