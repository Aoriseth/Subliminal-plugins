import requests
import re
import sys

title = sys.argv[1]
title = title.replace(" ", "+")
res = requests.get('https://www.google.com/search?client=firefox-b-d&q='+title+'+release+date')

searcher = re.compile("([0-9]{1,2} [a-z]* [0-9]{4})")
result = searcher.search(res.content.decode(res.encoding))
print(result.group(1))

