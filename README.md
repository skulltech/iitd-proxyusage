# iitd-proxylogin
Python script to check IIT Delhi proxy and wi-fi usage

## Installation

1. Clone the Repo: `$ git clone https://github.com/SkullTech/iitd-proxyusage.git`
2. `cd` into the Repo folder: `$ cd iitd-proxyusage`
3. Install the requirements: `$ pip3 install -r requirements.txt`

## Usage

As a script.
```
console
sumit@HAL9000:~/Sysadmin/iitd-proxyusage$ python3 checkusage.py 
[*] Enter username: cs5160400
[*] Enter password: 

Data usage for CS5160400, in MB

-----  ---------  -----
Proxy  yesterday      0
       week           0
       month          0
       year          85
Wi-Fi  monday      1151
       tuesday     1197
       wednesday   4282
       thursday    7063
       friday      3737
       saturday    3206
       sunday      2236
       week       22872
-----  ---------  -----
```

You can also import the proxyusage funtion and use it directly.
```
python
>>> from checkusage import proxyusage
>>> usage = proxyusage('cs5160400', 'notmyrealpassword')
>>> usage
{'proxy': {'yesterday': '0', 'week': '0', 'month': '0', 'year': '85'}, 'wifi': {'monday': '1151', 'tuesday': '1197', 'wednesday': '4282', 'thursday': '7063', 'friday': '3737', 'saturday': '3206', 'sunday': '2236', 'week': '22872'}}
```
