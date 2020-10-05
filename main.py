# nlp
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from urllib import request
import plotly.io as pio

URL = "https://en.wikipedia.org/wiki/Natural_language_processing"

page = request.urlopen(URL).read()

soup = BeautifulSoup(page, 'html.parser').get_text(strip=True).lower()

tokens = [i for i in soup.split()]
stop_words = stopwords.words('english')
clean_tokens = [i for i in tokens if i not in stop_words]

freq = nltk.FreqDist(clean_tokens)

high_freq = {i: x for i, x in freq.items() if x > 10}

fig = dict({
    "data": [{
        "type": "bar",
        "x": list(high_freq.keys()),
        "y": list(high_freq.values())
    }],
    "layout": {
        "title": {
            "text": "Most frequently used words in the page"
        },
        "xaxis": {"categoryorder": "total descending"}
    }
})

pio.show(fig)
