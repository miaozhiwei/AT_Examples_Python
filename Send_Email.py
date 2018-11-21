import smtplib
from email.mime.text import MIMEText

##################################################
mail_user = '***@qq.com'
mail_password = '***'
##################################################
mail_sender = mail_user
mail_receivers = u'***@qq.com'
##################################################
mail_subject = '这里是标题'
mail_content = '这里是内容'
##################################################

msg = MIMEText(mail_content)
msg['From'] = mail_sender
msg['To'] = mail_receivers
msg['Subject'] = mail_subject

try:
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.login(mail_user, mail_password)
    s.sendmail(mail_sender, mail_receivers, msg.as_string())
    print('邮件发送成功')
except Exception as e:
    print(e)
finally:
    s.quit()