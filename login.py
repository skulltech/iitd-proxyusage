import os
import requests
from getpass import getpass
from bs4 import BeautifulSoup

client_id = 'C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN'

username = input('Enter username: ') or 'cs5160400'
print(username)
password = getpass('Enter password: ')
os.environ['REQUESTS_CA_BUNDLE'] = os.getcwd() + '/CCIITD-CA.crt'

data = {'username': username, 'password': password, 'submit': ''}
params = {'response_type': 'code', 'client_id': client_id, 'state': 'xyz'}

headers = {
	'Referer': 'https://oauth.iitd.ac.in/login.php?response_type=code&client_id={}&state=xyz'.format(client_id),
}

session = requests.Session()

r = session.post('https://oauth.iitd.ac.in/authorize.php', data=data, params=params, headers=headers, allow_redirects=False)
redirect = r.headers['Location']
r = session.get(redirect, allow_redirects=False)

page = session.get('https://track.iitd.ac.in/data_usage.php')
soup = BeautifulSoup(page.text, 'html.parser')
elem = soup.select('html')
