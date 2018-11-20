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

API_ADDRESS = "http://api.openweathermap.org/data/2.5/weather?appid=f196d3f78dc2f7ac7f1318663aaba45e&q="

city = input("City Name, enter end to quit: ")

while city != "end":
	
	url = API_ADDRESS + city
	json_data = requests.get(url).json()

	#print(json_data)
	
	formatted_data = json_data['weather'][0]['description']
	formatted_data1 = json_data['weather'][0]['main']

	uppformatted = str(formatted_data)
	uppformatted1 = str(formatted_data1)

	print("Main report: " +uppformatted1.upper())
	
	print("Description of report: "+uppformatted.upper())
	
	city = input("City Name, enter end to quit: ")
	
	
	




