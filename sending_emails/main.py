# # import smtplib
# # #simple mail transfer protocol
# #
# # my_email = "ochemegmail.com"
# # password = "ochemeka08067543218"
# # message = "this is a text"
# #
# #
# # server = smtplib.SMTP("smtp.gmail.com", 587)
# # server.starttls()
# # server.login(user=my_email, password= password)
# #
# # server.sendmail(from_addr= my_email,
# #                     to_addrs="ochmelvin@gmail.com",
# #                     msg=message)
# #
# # server.close()
#
#
# import smtplib
# # server = smtplib.SMTP('smtp.gmail.com', 587)
# # server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
# # server = smtplib.SMTP('smtp.gmail.com:587')
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.ehlo()
# server.starttls()
#
# server.login('ochemeka@gmail.com', 'och08067543218')
# server.sendmail('ochemeka@gmail.com', 'ochmelvin@gmail.com', 'this is a python message')
# print('Mail Sent')




import os
import smtplib

EMAIL_ADDRESS = os.environ.get('ochemeka@gmail.com')
EMAIL_PAASWORD = os.environ.get('och08067543218')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PAASWORD)
    subject = 'grab a cup of tea'
    body = 'How was ur breakfast'
    msg = f'Subject: {subject}\n\n\{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'ochmelvin@gmail.com', msg)




# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.ehlo()
# server.starttls()
#
# server.login('ochemeka@gmail.com', 'och08067543218')
# server.sendmail('ochemeka@gmail.com', 'ochmelvin@gmail.com', 'this is a python message')
# print('Mail Sent')