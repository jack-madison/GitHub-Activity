import pandas as pd
import numpy as np
import requests
import gzip
import json
import ast

url = 'https://data.gharchive.org/2015-01-01-15.json.gz'

r = requests.get(url)

content = gzip.decompress(r.content).decode('utf-8')

dump = json.dumps(content)

data = json.loads(content)

text_file = open("./data.txt", "w")
text_file.write(dump)
text_file.close()

df = pd.DataFrame(data)