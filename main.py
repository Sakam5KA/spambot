import smtplib

user = 'sakam5ka@gmail.com'
password = 'sakampetka123'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, password)
print("Login success")

while True:
    server.sendmail(user, 'nhcfizika@yahoo.com', 'Bonjour. Sakam 5ka!')
