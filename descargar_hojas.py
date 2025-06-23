import datetime
import requests

fecha = datetime.datetime.now().strftime("%Y-%m-%d")

urls = {
    f"hoja1_{fecha}.csv": "https://docs.google.com/spreadsheets/d/17W6xwFXqmpcyG5y_2o3faXydPFQ_5H0yeTOrLfQz2jg/export?format=csv",
    f"hoja2_{fecha}.csv": "https://docs.google.com/spreadsheets/d/16h_ysa9Yde7ALrr4gFusl6gMhLcopVa23r_2I1_6MzI/export?format=csv"
}

for filename, url in urls.items():
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
