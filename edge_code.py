import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/HIDevolution-Zephyrus-Moonlight-Authorized-Performance/dp/B086Q99S3D?th=1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def check_price():
    page = requests.get(URL , headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser').get_text()

    price = str(soup.find( id="price_inside_buybox" ).get_text())
    price1 = float(price[0:5])

    if(price1<1599):
        send_mail()

    print(price1)

    if(price1>1599):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('edgeptoject.test@gmail.co','edgeprojecttest')

    subject = 'the price fell down'
    body = ''

    msg= f"subject:{subject}\n\n{body}"

    server.sendmail(
        'edgeproject.test@gmail.com',
        'edgeproject.test@gmail.com',
        msg
    )

    print('hey email sent')
    server.quit()






