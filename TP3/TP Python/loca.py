### Créateur : Matéo CROIX
### Date : 20/09/2022

### Objectif : Création d'un programme qui extrait des IPS d'un fichier log et localiser les ip sur une map.

import sys, re
import geocoder
import pandas as pd
import folium


f = open("TP PYTHON/access.log.txt",'r')
text = f.read()


ips = [] 
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:

            current_ip = {
                'ip':match,
                'Latitude':"",
                'Longitude':"",
            }
            loca = geocoder.ip(match)
            current_ip["Latitude"] = loca.lat
            current_ip["Longitude"] = loca.lng

            ips.append(current_ip)

print(ips)


def supprimeDoublon(current_ip):
    for i in current_ip:
        if i not in current_ip:
            current_ip.append(i)
        return

m = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")

tooltip = "Click me!"

for ip in ips:
    folium.Marker(
        [ip["Longitude"], ip["Latitude"]], popup=ip["ip"], tooltip=tooltip
    ).add_to(m)

m.save("index.html")