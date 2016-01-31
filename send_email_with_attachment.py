import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "shaunak06@gmail.com"
gmail_pwd = "swimmer555"

def mail(to, text, attach):
  msg = MIMEMultipart()

  msg['From'] = gmail_user
  msg['To'] = to
  msg['Subject'] = 'Thank you for coming to my grad party!'

  msg.attach(MIMEText(text))
  if attach != "":
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach + '.JPG', 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
            'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

  mailServer = smtplib.SMTP("smtp.gmail.com", 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmail_user, gmail_pwd)
  mailServer.sendmail(gmail_user, to, msg.as_string())
  # Should be mailServer.quit(), but that crashes...
  mailServer.close()

fin = open(r"C:\Users\Shaunak\Desktop\poo2.csv","r")
fin.readline() #remove header
for row in fin:
    c=row.split(",")
    print c
    mail(c[1].strip(),
        'Dear '+ c[0] + ',\nThank you very much for coming to my graduation party.\nIt was great that you were able to make it and I enjoyed the time with you.\n' + c[2] +'\n\nShaunak Pandit\n\nSent using Python.',
        c[3].strip())
    