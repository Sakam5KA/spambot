import os
import sys
import smtplib
from time import sleep

user = 'vdzhashendechko@gmail.com'
password = 'and2302ban1504'

while True:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    print("Login success")
    server.sendmail(user, 'stojanovskaslagjana@yahoo.fr', 'Bonjour. Sakam 5ka!')
    print("mail sent!")
    server.quit()
    sleep(2)
    
    
    #    try:
#        server.sendmail(user, 'nhcfizika@yahoo.com', 'Bonjour. Sakam 5ka!')
#        print("mail sent!")
#        sleep(1)
#    except Exception as e:
#        print("error!")
#        sleep(60)
