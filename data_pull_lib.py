import pandas as pd
from gharchive import GHArchive

gh = GHArchive()

data = gh.get('6/8/2020', '6/8/2020', filters=[
    ('repo.name', 'bitcoin/bitcoin'),
    ('type', 'WatchEvent')
])

type(data)

df = pd.DataFrame(data)



from gzip import decompress
from json import loads

from requests import get

url = 'https://data.gharchive.org/2020-01-01-15.json.gz'

def get_gzipped_json(url):
    return loads(decompress(get(url).content))

if __name__ == '__main__':
    print(get_gzipped_json("https://xxxxx.auth0.com/1537150574"))

github = get_gzipped_json(url)