import eel #подключение библиотеки веб интерфесов
import pyowm #подключение библиотеки для взаимодействия с API OpenWeatherMap
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = pyowm.OWM("f17480b84563d8c6cde6484c071ca775") 

@eel.expose #говорим что эту функцию можно использовать с js
def get_weather(place):#Описание функции с аргументом place = город который мы выбрали
	city = place #присваиваем город к переменной city
	mgr = owm.weather_manager() #присваиваем модуль api к переменной mgr
	observation = mgr.weather_at_place(city) # присваиваем mgr+погода для города
	w = observation.weather 

	temp = w.temperature('celsius')['temp']
	result1 = "<li>" + "<span>" + "Температура: "+ "</span>" + "<img src='img/temperature.png'>" + str(temp)+ "℃" + "</li>"

	details = w.detailed_status
	result2 = "<li>" + "Погода: " + str(details) + "</li>"

	wind = w.wind()['speed']
	result3 = "<li>" + "Ветер: " + str(wind) + " м/с" + "</li>"

	humidity = w.humidity
	result4 = "<li>" + "Влажность: " + str(humidity) + "%" + "</li>"

	clouds = w.clouds
	result5 = "<li>" + "Осадки: " + str(clouds) + "</li>"

	result = "<ul>"+result1+result2+result3+result4+result5+"</ul>"

	return result

#Вывод Окна веб приложения

eel.init("web") #Создание окна веб приложения
eel.start("main.html", size=(700, 700))#исполняемый html файл для окна веб приложения