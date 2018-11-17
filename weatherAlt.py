import pyowm

owm = pyowm.OWM('f196d3f78dc2f7ac7f1318663aaba45e')

observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w)
