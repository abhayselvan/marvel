import os
import time
import json
from hashlib import md5

import requests  

# getting this from env variables, you can replace them with your
# values, but keep the private key private!
PUBLIC_KEY = os.getenv('MARVEL_PUBLIC_KEY')
PRIVATE_KEY = os.getenv('MARVEL_PRIVATE_KEY')


CHARACTER_URL = 'http://gateway.marvel.com/v1/public/characters'


def get_hash_and_ts_params():
    ts = str(time.time())
    combined = ''.join([ts, PRIVATE_KEY, PUBLIC_KEY])
    hash_value = md5(combined.encode('ascii')).hexdigest()
    return {'ts': ts, 'hash': hash_value}


def paged_requests(page_size=100):
    params = {'apikey': PUBLIC_KEY, 'limit': page_size}
    for i in range(15):
        hash_params = get_hash_and_ts_params()
        params.update(hash_params)
        params.update({'offset': page_size * i}) # offset, how many records to skip
        resp = requests.get(CHARACTER_URL, params)
        #print(f'Requested page {i} of {page_size} records')
        resp.raise_for_status()  # stop if there are any errors!
        #print(f'Full request URL: {resp.request.url}')
        j = resp.json()
        marvel_characters.append(j)
        #first_ten = [a['name'] for a in j['data']['results']][:10]
        #print(f'First ten records: {first_ten}')
    #print('Done')
    


if __name__ == '__main__':
    marvel_characters = []
    marvel = {}                                                                                                                                                                                                                                                          
    paged_requests()
    marvel = { 'marveldict': marvel_characters }

    with open('marvel_characters.json','w') as f:
        json.dump(marvel, f, indent=2)

