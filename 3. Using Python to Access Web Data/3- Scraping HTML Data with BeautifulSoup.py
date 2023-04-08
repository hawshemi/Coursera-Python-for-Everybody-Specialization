from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser

soup = BeautifulSoup(html, "html.parser")
sumnum = list()

# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag (just for fun)
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    x = tag.contents[0]
    sumnum.append(int(x))
print(sum(sumnum))