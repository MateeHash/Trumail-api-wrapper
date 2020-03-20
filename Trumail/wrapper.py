import requests
from xml.etree import cElementTree as ET
import json


def lookup(email):
    if type(email) != str:
        raise TypeError("Email must be a string")
    request = requests.get(f"https://api.trumail.io/v2/lookups/json?email={email}")
    response = request.text
    return json.loads(response)


    
    
