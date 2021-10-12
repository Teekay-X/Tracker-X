import os
import urllib.request
import json
import time
os.system("clear")
logo = """ \u001b[33m
  ______                    __
 /_  __/_____ ____ _ _____ / /__ ___   _____        _  __
  / /  / ___// __ `// ___// //_// _ \ / ___/______ | |/_/
 / /  / /   / /_/ // /__ / ,<  /  __// /   /_____/_>  <
/_/  /_/    \__,_/ \___//_/|_| \___//_/          /_/|_|
\u001b[32m###Git		:github.com/Teekay-X
###IG		:asahluma.mabhongo
###FB		:T e e k a y - X
=======================================================
           	\u001b[35mPRESS CTRL + Z TO EXIT\u001b[30m
"""
print (logo)
try:

 ip = input("\u001b[31mEnter target IP:")
 url = "https://ip-api.com/"
 response = urllib.request.urlopen(url + ip)
 data = response.read()
 values = json.loads(data)
 print ("\n")
 while True: 
   print ("Tracing :" + ip )
   time.sleep(2)

   print ("IP Adrress:" + values ["query"])
   print ("Status:" + values ["status"])
   print ("Continent:" + values ["continent"])
   print ("ContinentCode:" + values ["continentCode"])
   print ("Country:" + values ["country"])
   print ("CountryCode:" + values ["countryCode"])
   print ("Region:" + values ["region"])
   print ("RegionName:" + values ["regionName"])
   print ("City:" + values ["city"])
   print ("District:" + values ["district"])
   print ("Zip:" + values ["zip"])
   print ("Latitude:" + values ["lat"])
   print ("Longitude:" + values ["lon"])
   print ("TimeZone:" + values ["timezone"])
   print ("OfSet:" + values ["offset"])
   print ("Currency:" + values ["currency"])
   print ("ISP:" + values ["isp"])
   print ("Org:" + values ["org"])
   print ("As:" + values ["as"])
   print ("Asname:" + values ["asname"])
   print ("Mobile:" + values ["mobile"])
   print ("Proxy:" + values ["proxy"])
   print ("Hosting:" + values["hosting"])
   break
except Exception or KeyboardInterrupt as err:
   print (f"\033[32m [\033[31m ! \033[32m] \033[31m  {err}")
if ip == '':
 print ("\u001b[34mEnter ip bruh!!")

ex = input("\u001b[33m[~]Enter \u001b[37m'X'\u001b[35m to continue >>>")

if ex == "X" or "x":
 print ("\n")
 print ("\u001b[35m EXITING......")
 time.sleep(3)
 print ("\n")
 exit(1)
else:
 print ("\n")
 print ("\u001b[32m I said X  not " + ex)
 print ("\n")
 exit(1)
