#  install libraries and dependencies
#  install parser - lxml (pip install lxml)

import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Titanic-120338"
response = requests.get(website)
content = response.text  # For getting the content of website

soup = BeautifulSoup(content, 'lxml') # soup is what we get after using the parser (i.e. we will get the html code of website). Here I have used lxml.
html = soup.prettify()
print(html)
