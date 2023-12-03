import requests
import re

def findH3Headlines(url):
  data = requests.get(url).text
  print(re.findall(r'<h3[^>]*>(.*?)</h3>', data))

findH3Headlines('http://www.columbia.edu/~fdc/sample.html')
