import smtplib
from time import sleep

user = 'sakam5ka@gmail.com'
password = 'sakampetka123'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(user, password)
print("Login success")

while True:
    try:
        server.sendmail(user, 'nhcfizika@yahoo.com', 'Bonjour. Sakam 5ka!')
        print("mail sent!")
        sleep(1)
    except Exception as e:
        print("pause!")
        sleep(60)
