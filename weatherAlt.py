import pyowm

owm = pyowm.OWM('f196d3f78dc2f7ac7f1318663aaba45e')
observation = owm.weather_at_place("Cambridge,uk")
w = observation.get_weather()
temperature = w.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()
wind = w.get_wind()
print(w)
print(wind)
print(temperature)
print(tomorrow)