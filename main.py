# nlp
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from urllib import request
import plotly.io as pio

URL = "https://en.wikipedia.org/wiki/Natural_language_processing"

page = request.urlopen(URL)

html_plain = page.read()
soup = BeautifulSoup(html_plain, 'html.parser')
soup_text = soup.get_text(strip=True)
ready_text = soup_text.lower()

tokens = [i for i in ready_text.split()]
stop_words = stopwords.words('english')
clean_tokens = [i for i in tokens if i not in stop_words]

freq = nltk.FreqDist(clean_tokens)

high_freq = dict()

for key, val in freq.items():
    if (val > 10):
        high_freq[key] = val

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
