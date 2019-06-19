import requests
import json

api_key = 'AIzaSyBgLnebInihBBk_qifMc7tcZcQ57T4RcyY'
url = 'https://maps.googleapis.com/maps/api/geocode/json?'

res_ob = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=New+york&key="API_ID"')
x = res_ob.json()
print(x)
