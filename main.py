import eel
import pyowm

owm = pyowm.OWM("f17480b84563d8c6cde6484c071ca775")

@eel.expose
def get_weather(place):
	city = place
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(city)
	w = observation.weather

	temp = w.temperature('celsius')['temp']

	return "В городе " + city + " сейчас " + str(temp) + " градусов!"

#Вывод Окна веб приложения

eel.init("web")
eel.start("main.html", size=(500, 500))