import typer 
import random 
import time 
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import os 
import folium
from colorama import Fore
from colorama import init 
from opencage.geocoder import OpenCageGeocode

#app
app = typer.Typer()

#key 
key = "7e5552da788f400db1f3f51cd584933f"

 #scanning phone number 
@app.command()
def number(phone):
    os.system("clear")
    print(Fore.GREEN + "Scanning Number: " + Fore.WHITE + phone)
    info_numb = phonenumbers.parse(phone, "CH")
    print(Fore.GREEN+ "Info: " + Fore.WHITE + str(info_numb))
    place = geocoder.description_for_number(info_numb, "en")
    print(Fore.GREEN + "Location: " + Fore.WHITE + place)
    service = phonenumbers.parse(phone, "RO")
    print(Fore.GREEN + "Carrier: " + Fore.WHITE +carrier.name_for_number(service, "en"))
    time = phonenumbers.parse(phone, "en")
    print(Fore.GREEN + "timezone: " + Fore.WHITE + str(timezone.time_zones_for_number(time)))
    cordinat = OpenCageGeocode(key)
    idk = str(place)
    place_number = cordinat.geocode(idk)
    p_1 = place_number[0]['geometry']['lat']
    p_2 = place_number[0]['geometry']['lng']
    cord1 = str(p_1)
    cord2 = str(p_2)
    print(Fore.GREEN + "Cordinats: " + Fore.WHITE + cord1 + " " + cord2)
    print(Fore.WHITE)
    print("")

#showing Ip info 
@app.command()
def ip(ipaadr):
    import geocoder
    os.system("clear")
    g = geocoder.ip(ipaadr)
    addres = g.latlng
    map_co = folium.Map(location=addres, zoom_start=12)
    folium.CircleMarker(location=addres, radius=50, popup="Yorkshire").add_to(map_co)
    folium.Marker(addres, popup="Yorkshire").add_to(map_co)
    print(Fore.GREEN + "latlng: " + Fore.WHITE + str(addres))
    print(Fore.GREEN + "map has saved: " + Fore.WHITE + "iplocation.html")
    print("")
    map_co.save("iplocation.html")
    

#info
@app.command()
def about():
    os.system("clear")
    print(Fore.MAGENTA)
    print(""" 
  /$$$$$$                                                                                                     
 /$$__  $$                                                                                                    
| $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
| $$  | $$|  $$  /$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$ /$$__  $$
| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/|  $$$$$$ | $$$$$$$$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  | $$| $$$$$$$$
| $$  | $$  \  $$$/ | $$_____/| $$       \____  $$| $$_____/| $$_____/| $$  | $$| $$_____/| $$  | $$| $$_____/
|  $$$$$$/   \  $/  |  $$$$$$$| $$       /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/     \_/    \_______/|__/      |_______/  \_______/ \_______/|__/  |__/ \_______/ \____  $$ \_______/
                                                                                           /$$  | $$          
                                                                                          |  $$$$$$/          
                                                                                           \______/           
                                                                                                               """)
    print("")
    print(Fore.WHITE)
    print("enter --help for commands")
    print(Fore.CYAN)
    print("Creator: Frninezy")
    print(Fore.BLUE)
    print("Github: https://github.com/FRNINEZY")
    print(Fore.YELLOW)
    print("Buy coffe for me(xmr[my manero]): 47AdWJEZUq7DkoFqPS78rT5b1k4BMoNULdNpCqFPpqay4JNWyCRgLW5FgkbD7SCb35gBB1EerrTh5PXJU32Le1SvEr7uKqS")
    print(Fore.GREEN)
    print("Made in 2022")
    print("")

if __name__ == "__main__":
    app()