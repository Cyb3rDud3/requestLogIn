import requests
import random
import time


for i in range(999999):
    try:
       #Configure your own username\password combination
       passlock = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
       conf = ['#', '@', '^', '&', '*', '!', '?', '#',]
       c = random.choice(conf)
       r = random.choice(passlock)
       r1 = random.choice(passlock)
       r2 = random.choice(passlock)
       r3 = random.choice(passlock)
       r4 = random.choice(passlock)
       r5 = random.choice(passlock)
       com = '@gmail.com'
       name = random.choice(passlock) +r +r1 +r2 +r3 +r4 +r5 +str(random.randrange(1,8888)) + com
       password = str(c) + str(r) + r1 + r2 +r3 +r4 +r5 +r1 + str(random.randrange(1, 99999))
       url = 'str'
       #configure username\passcode elements
       payload = {'UserNameElement': name, 'PassCodeElement': password}
       r = requests.post(url, data=payload)
       print(f'logging in to {url}, username: {name}, password: {password}')
       print (f'response: \n{r.content}')
    except Exception as e:
    	print(f'error: {e}')
