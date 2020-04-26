import requests
from utils.config import read_yaml

config = read_yaml()


def get(path, params):
    url = config['url'] + path
    response = requests.get(url, headers=config['head'], params=params)
    return response.json()


def post(path, params):
    url = config['url'] + path
    response = requests.post(url, headers=config['head'], params=params)
    return response.json()
