from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from getpass import getpass
import requests


client_id = 'C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN'

username = input('Enter username: ') or 'cs5160400'
print(username)
password = getpass('Enter password: ')

data = {'username': username, 'password': password, 'submit': ''}
params = {'response_type': 'code', 'client_id': client_id, 'state': 'xyz'}
headers = {
	'Referer': 'https://oauth.iitd.ac.in/login.php?response_type=code&client_id={}&state=xyz'.format(client_id),
}

session = requests.Session()

r = session.post('https://oauth.iitd.ac.in/authorize.php', data=data, params=params, headers=headers, verify=False, allow_redirects=False)
redirect = r.headers['Location']
r = session.get(redirect, verify=False, allow_redirects=False)

resp = session.get('https://track.iitd.ac.in/data_usage.php')
print(resp.text)


# oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
# token = oauth.fetch_token(token_url='https://oauth.iitd.ac.in/authorize.php', username=username, password=password)
# print(token)