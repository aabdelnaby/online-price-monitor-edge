import requests
from bs4 import BeautifulSoup
import smtplib
import time
#URL of product website
URL = 'https://www.ebay.com/p/12029450068?iid=143516507543&var=442474017408'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

## this function grabs the price of a product from an online store (ebay in this case)
def check_price():

    page = requests.get(URL , headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser')

    cost = soup.find(id="tab-panel-0-w3").get_text()

#cost of product is taken from html sting and reassigned  into price as a float
    price = float(cost[1:4])

    if price<374:
        send_mail_down()

    if price>374:
        send_mail_up()

    if price==374:
        send_mail_same()


##these three functions are responsible for sending emails
def send_mail_down():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('edgeproject.test@gmail.com','edprojecttest')

    subject = 'product price decreased'
    body = 'check the link out https://www.ebay.com/p/12029450068?iid=143516507543&var=442474017408'

    msg= f"subject:{subject}\n\n{body}"

    server.sendmail(
        'edgeproject.test@gmail.com',
        'edgeproject.test@gmail.com',
        msg
    )

    print('email sent')
    server.quit()

def send_mail_up():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('edgeproject.test@gmail.com','edprojecttest')

    subject = 'product price increased, do not buy now'
    body = 'check the link out https://www.ebay.com/p/12029450068?iid=143516507543&var=442474017408'

    msg= f"subject:{subject}\n\n{body}"

    server.sendmail(
        'edgeproject.test@gmail.com',
        'edgeproject.test@gmail.com',
        msg
    )

    print('email sent')
    server.quit()

def send_mail_same():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('edgeproject.test@gmail.com','edprojecttest')

    subject = 'product price did not change'
    body = 'check the link out https://www.ebay.com/p/12029450068?iid=143516507543&var=442474017408'

    msg= f"subject:{subject}\n\n{body}"

    server.sendmail(
        'edgeproject.test@gmail.com',
        'edgeproject.test@gmail.com',
        msg
    )

    print('email sent')
    server.quit()

##calls for check_price function and sets how frequently is the price checked
while True:
    check_price()
    time.sleep(60*60*24)



