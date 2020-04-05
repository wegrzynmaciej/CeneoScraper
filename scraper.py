#import bibliotek
import requests
from bs4 import beautifulsoup
#pobranie kodu pojedynczej strony z opiniami o produkcie
url - "https://www.ceneo.pl/85910996#tab=reviews"
response = requests.get(url)