import os
import ipinfo
import subprocess as sb
import time
from colorama import init, Fore

try:
	import requests
except:
  print("У вас не установлена библиотека requests. Сейчас она установится сама...")
	os.system('pip install requests')
	import requests

try:
	from bs4 import BeautifulSoup as bs4
except:
  print("У вас не установлена библиотека bs4. Сейчас она установится сама...")
	os.system('pip install bs4')
	from bs4 import BeautifulSoup as bs4

def clear_console(): os.system("cls" if os.name == "nt" else "clear")

def main():
	access_token = "40fff983f832fa"
	while True:
		clear_console()
		ip = input(" Введите IP-адресс >> ")
		try:
			handler = ipinfo.getHandler(access_token)
			details = handler.getDetails(ip)
		except Exception as e:
			print("Простите, произошла непредвиденная ошибка, попробуйте ещё раз"); time.sleep(1); continue

		try:
			print(f"""
			MAIN INFO

			|IP | {getattr(details, 'ip', 'не найдено')} |
			| HOSTNAME | {getattr(details, 'hostname', 'не найдено')} |
			| CITY | {getattr(details, 'city', 'не найдено')} |
			| REGION | {getattr(details, 'region', 'не найдено')} |
			| COUNTRY | {getattr(details, 'country', 'не найдено')} |
			| LOC | {getattr(details, 'loc', 'не найдено')} |
			| ORG | {getattr(details, 'org', 'не найдено')} |
			| TIMEZONE | {getattr(details, 'timezone', 'не найдено')} |
			""")
		except:
			print("Непредвиденная ошибка... Попробуйте снова"); time.sleep(1); continue

		url = 'https://ip2geolocation.com/?ip=' + str(ip)
		print('          URL Для просмотра: ' + str(url))
		input("\n\nНажмите ENTER для продолжения")

if __name__ == "__main__":
	main()
