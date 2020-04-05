# Import bibliotek
import requests
from bs4 import BeautifulSoup

# Pobranie kodu pojedynczej strony z opiniami o produkcie
url = "https://www.ceneo.pl/85910996#tab=reviews"
response = requests.get(url)
page_dom = BeautifulSoup(response.text, 'html.parser')

# Wyciągnięcie z kodu strony fragmentów odpowiadających poszczególym opiniom
opinions = page_dom.select("li.js_product-review")

opinion = opinions.pop(0)

# Zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii
opinion_id = opinion["data-entry-id"]
author = opinion.select("div.reviewer-name-line").pop().text.strip()
recommendation = opinion.select(
    "div.product-review-summary > em").pop().text.strip()
stars = opinion.select("span.review-score-count").pop().text.strip()
content = opinion.select("p.product-review-body").pop().text.strip()
try:
    cons = opinion.select("div.cons-cell > ul").pop().text.strip()
except IndexError:
    cons = None
try:
    pros = opinion.select("div.pros-cell > ul").pop().text.strip()
except IndexError:
    pros = None

useful = opinion.select("button.vote-yes > span").pop().text.strip()
useless = opinion.select("button.vote-no > span").pop().text.strip()
opinion_date = opinion.select(
    'span.review-time > time:nth-child(1)').pop()["datetime"].strip()
try:
    purchase_date = opinion.select(
        'span.review-time > time:nth-child(2)').pop()["datetime"].strip()
except IndexError:
    purchase_date = None


features = {
    "opinion_id": opinion_id,
    "author": author,
    "recommendation": recommendation,
    "stars": stars,
    "content": content,
    "cons": cons,
    "pros": pros,
    "useful": useful,
    "useless": useless,
    "opinion_date": opinion_date,
    "purchase_date": purchase_date
}


print(features)
