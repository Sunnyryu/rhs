from decouple import config
import requests
from pprint import pprint




token = config('TOKEN')
base_url = f'https://api.telegram.org/bot{token}'
url = "ssunyryu1.pythonanywhere.com"
setweb_url = f'/setwebhook?url={url}'

req = requests.get(base_url+setweb_url).json()

pprint(req)