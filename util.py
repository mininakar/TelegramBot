import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# api_url = 'https://api.telegram.org/6176884644:AAE8459aNh1EWgxVSU1YZL9R5EpIc_K79bc/getMe'

class Get_dog:

    def __init__(self):
        self.url = 'https://random.dog/woof.json'


    def get_file_json(self):
        response = requests.get(self.url)
        return response.json().get('url')

