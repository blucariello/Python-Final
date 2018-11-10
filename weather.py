#!/usr/bin/python3
"""
__author__ = "Brandon Lucariello"
__copyright__ = "cc"
__credits__ = ["Brandon Lucariello"]
__license__ = "cc"
__version__ = "0.1"
__maintainer__ = "Brandon Lucariello"
__email__ = "blucariello@my365.bellevue.edu"
__status__ = "testing"
"""

import requests

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=f196d3f78dc2f7ac7f1318663aaba45e&q="
city = input("City Name: ")

url = api_address + city

json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['description']

print(formatted_data)