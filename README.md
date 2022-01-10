# Overseeneye-cli

Overseeneye-cli is a simple command line tool for Linux/Unix. With it you can scan phonenubers and track ip address location.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install typer
pip install phonenumbers
pip install folium
pip install opencage
pip install geocoder
pip install colorama
```
## Setup

Just copy repo and create a folder(name: overseeneye) on your desktop

cd Desktop

cd overseeneye




## Usage Numbers

```bash
user@user-desktop:~/Desktop/overseeneye$ python3 overseeneye.py number +16503858068

Scanning Number: +16503858068
Info: Country Code: 1 National Number: 6503858068
Location: California
Carrier: 
timezone: ('America/Los_Angeles',)
Cordinats: 36.7014631 -118.755997
```

## Usage IP

```bash
user@user-desktop:~/Desktop/overseeneye$ python3 overseeneye.py ip 

latlng: [37.5483, -121.9886]
map has saved: iplocation.html
```

