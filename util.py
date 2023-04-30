import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json



class Get_dog:

    def __init__(self):
        self.url = 'https://random.dog/woof.json'


    def get_file_json(self):
        response = requests.get(self.url)
        return response.json().get('url')

