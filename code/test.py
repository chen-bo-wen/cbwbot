print('111')
import requests
url = "https://ctfserver.hkbu.app/coupon/"

response = requests.get(url)
print('res', response)
