import requests
import lxml.html
from bs4 import BeautifulSoup

def cas_login(email, password):

    s = requests.session()
    login = s.get('https://cm.litextension.com/login')
    login_html = lxml.html.fromstring(login.text)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    form['email'] = email
    form['password'] = password
    response = s.post('https://cm.litextension.com/login', data=form)
    print(response.url)
    return response

def getName(response):
    Soup = BeautifulSoup(response.text,"lxml")
    return Soup.find('a',id='navbarDropdown2').text


email= 'test1@test.com'
password='aA123456'

response=cas_login(email,password)
print(getName(response))
