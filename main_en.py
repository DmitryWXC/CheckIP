import os
import ipinfo
import subprocess as sb
import time
from colorama import init, Fore

try:
	import requests
except:
  print("You don't have the requests library installed. Now it will establish itself...")
	os.system('pip install requests')
	import requests

try:
	from bs4 import BeautifulSoup as bs4
except:
  print("You don't have the bs4 library installed. Now it will establish itself...")
	os.system('pip install bs4')
	from bs4 import BeautifulSoup as bs4

def clear_console(): os.system("cls" if os.name == "nt" else "clear")

def main():
	access_token = "40fff983f832fa"
	while True:
		clear_console()
		ip = input(" Input ip-adress >> ")
		try:
			handler = ipinfo.getHandler(access_token)
			details = handler.getDetails(ip)
		except Exception as e:
			print("Sorry, there was an unexpected error, try again"); time.sleep(1); continue

		try:
			print(f"""
			MAIN INFO

			|IP | {getattr(details, 'ip', 'not found')} |
			| HOSTNAME | {getattr(details, 'hostname', 'not found')} |
			| CITY | {getattr(details, 'city', 'not found')} |
			| REGION | {getattr(details, 'region', 'not found')} |
			| COUNTRY | {getattr(details, 'country', 'not found')} |
			| LOC | {getattr(details, 'loc', 'not found')} |
			| ORG | {getattr(details, 'org', 'not found')} |
			| TIMEZONE | {getattr(details, 'timezone', 'not found')} |
			""")
		except:
			print("Unexpected error... Try again"); time.sleep(1); continue

		url = 'https://ip2geolocation.com/?ip=' + str(ip)
		print('          URL for watching: ' + str(url))
		input("\n\nPress enter to continue")

if __name__ == "__main__":
	main()
