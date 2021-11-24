import json

from .companias.models import Compania

with open('data.json') as file:
    data = json.load(file)
    print(data[0])
