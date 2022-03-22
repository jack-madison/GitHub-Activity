import pandas as pd
import numpy as np
import requests
import gzip
import json
import ast

url = 'https://data.gharchive.org/2021-01-01-15.json.gz'

r = requests.get(url)

content = gzip.decompress(r.content).decode('utf-8')

dump = json.dumps(content)

res = ast.literal_eval(dump)

res = res.replace(":false", ":False")
res = res.replace(":true", ":True")



dict = json.loads(res)

df = pd.DataFrame(res)
