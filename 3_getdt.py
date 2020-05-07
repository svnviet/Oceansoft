Key ='63250ac0afd68cccd81f5383228b83df'
Pass ='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'
version='2020-04'
Name='my-dev-shop-12'

shop_url = "https://%s:%s@%s.myshopify.com/admin/api/%s" % (Key, Pass, Name, version)

import requests
response=requests.get(shop_url+'/customers.json').json()

for i in range(len(response['customers'])):
    if 'addresses' in response['customers'][i]:
        del response['customers'][i]['addresses']
    if 'default_address' in response['customers'][i]:
        del response['customers'][i]['default_address']


import json
with open('data.csv', 'w') as outfile:
    json.dump(response, outfile)
