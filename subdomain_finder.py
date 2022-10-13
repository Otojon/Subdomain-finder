#!/usr/bin/env python3
# v 1.0


import requests
print(  "  ______   _______   __    __  ______ ____",  
 "\n /      \ |\      \ |\ \  |\ \|\     \    \ ", 
"\n|  $$$$$$\| $$$$$$$\| $$  | $$| $$$$$$\$$$$ ",
"\n| $$    $$| $$  | $$| $$  | $$| $$ | $$ | $$",
"\n| $$$$$$$$| $$  | $$| $$__/ $$| $$ | $$ | $$",
 " \n \$$     \| $$  | $$ \$$    $$| $$ | $$ | $$",
  "\n  \$$$$$$$ \$$   \$$  \$$$$$$  \$$  \$$  \$$"
  ,"by @otojonxudayarov"
                                            )
#ask domain name
domain=str(input("enter domain name(for example => google.com): "))
#use  valid text file to enumerate
file=open("subdomains.txt")
sub=file.read()
#split the new lines
subdomains=sub.splitlines()
founded_domains=[]
print("please wait...")
for subdomain in subdomains:
    #build the url :)
    url=f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        #if subdomain doesn't exist it just passes
        pass
    else:
        print("[+]found :", url)
        #append discoveries to created list 
        founded_domains.append(url)