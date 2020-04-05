# Ceneo-Scrapper
## Etap 1 - Analiza struktury opinii w serwisie [Ceneo](https://ceneo.pl)
|Składowa             |Selektor                                            |Nazwa zmiennej|
|---------------------|----------------------------------------------------|--------------|
|Opinia               |`li.js-product-review`                              |`opinion`
|Identyfikator opinii |`["data-entry-id"]`                                 |`opinion_id`
|Autor                |`div.reviewer-name-line`                            |`author`
|Rekomendacja         |`div.product-review-summary > em`                   |`recommendation`
|Ocena                |`span.review-score-count`                           |`stars`
|Treść opinii         |`p.product-review-body`                             |`content`
|Lista wad            |`div.cons-cell > ul`                                |`cons`
|Lista zalet          |`div.pros-cell > ul`                                |`pros`
|Przydatna            |`button.vote-yes > span`                            |`useful`
|Nieprzydatna         |`button.vote-no > span`                             |`useless`
|Data wystawienia     |`span.review-time > time:first-child["datetime"]`  |`opinion_date`
|Data zakupu          |`span.review-time > time:nth-child(2)["datetime"]` |`purchase_date`
## Etap 2 - pobranie składowych pojedynczej opinii
- Pobranie kodu jednej strony z opiniami o konkretnym produkcie
- Wyciągnięcie z kodu strony fragmentów odpowiadających poszczególym opiniom
- Zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- Zapisanie do złożonej struktury danych składowych wszystkich opinii z pojedynczej strony
- Przechodzenie po kolejnych stronach z opiniami
- Zapis wszystkich opinii o pojedynczym produkcie do pliku
