# iitd-proxylogin
Python script to check IITD proxy usage

## Installation

1. Clone the Repo: `git clone https://github.com/SkullTech/iitd-proxyusage.git`
2. Install the requirements: `pip3 install -r requirements.txt`

## Usage

As a script.
```
sumit@sumit-HP-Pavilion-Notebook:~/iitd-proxyusage$ python3 checkusage.py
Enter username: cs5160400
Enter password: 

Data Usage for CS5160400

---------  --------
Yesterday  34MB
Week       9205MB
Month      30171MB
Year       196500MB
---------  --------
```

You can also import the proxyusage funtion and use it directly.
```
>>> from checkusage import proxyusage
>>> usage = proxyusage('cs5160400', 'notmyrealpassword')
>>> usage
{'month': '30171MB', 'yesterday': '34MB', 'year': '196500MB', 'week': '9205MB'}
```
