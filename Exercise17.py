#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
aot_url = 'https://en.wikipedia.org/wiki/Attack_on_Titan'

# Sending a request to the URL
r = requests.get(aot_url)
r_html = r.text

# Parsing the HTML content
soup = BeautifulSoup(r_html, 'html.parser')

# Find all headings (h1, h2, h3, etc.)
# You can adjust the range depending on the depth of titles you want
for i in range(1, 4):
    headings = soup.find_all(f'h{i}')
    for heading in headings:
        # Extracting the text from each heading
        print(heading.get_text().strip())


