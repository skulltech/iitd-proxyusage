import os
import requests
import warnings
import sys
from getpass import getpass
from bs4 import BeautifulSoup
from tabulate import tabulate

CLIENT_ID = 'C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN'


def proxyusage(username, password):
    """Returns the IITD proxyusage data.

    Parameters
    ----------
    username: str, Kerberos ID
    password: str, Kerberos Password

    Returns
    -------
    dict
        dict with proxyusage data. The keys of this dict are 'yesterday', 'week', 'month' and 'year'.
    """

    data = {
        'username': username, 
        'password': password, 
        'submit': ''
    }
    params = {
        'response_type': 'code', 
        'client_id': CLIENT_ID, 
        'state': 'xyz'
    }
    headers = {
        'Referer': 'https://oauth.iitd.ac.in/login.php?response_type=code&client_id={}&state=xyz'.format(CLIENT_ID)
    }
    session = requests.Session()
    r = session.post('https://oauth.iitd.ac.in/authorize.php', data=data, params=params, headers=headers, allow_redirects=False)
    redirect = r.headers['Location']
    try:
        r = session.get(redirect, allow_redirects=False)
    except requests.exceptions.MissingSchema:
        return False

    page = session.get('https://track.iitd.ac.in/data_usage.php')
    soup = BeautifulSoup(page.text, 'html.parser')
    elems = soup.select('td[align="right"]')[4:]
    usage = {
        'proxy': {
            'yesterday': elems[0].text, 
            'week': elems[1].text, 
            'month': elems[2].text, 
            'year': elems[3].text
        },
        'wifi': {
            'monday': elems[12].text,
            'tuesday': elems[13].text,
            'wednesday': elems[14].text,
            'thursday': elems[15].text,
            'friday': elems[16].text,
            'saturday': elems[17].text,
            'sunday': elems[18].text,
            'week': elems[19].text,
        }
    }
    return usage


def main():
    username = input('[*] Enter username: ')
    password = getpass('[*] Enter password: ')

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        usage = proxyusage(username, password)

    if not usage:
        print('Invalid credentials!')
        sys.exit()

    print('\nData usage for {}, in MB\n'.format(username.upper()))
    l1 = [['', key, value] for key, value in usage['proxy'].items()]
    l1[0][0] = 'Proxy'
    l2 = [['', key, value] for key, value in usage['wifi'].items()]
    l2[0][0] = 'Wi-Fi'
    print(tabulate(l1+l2))


if __name__ == '__main__':
    main()
