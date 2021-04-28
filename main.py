import eel #подключение библиотеки веб интерфесов
import pyowm #подключение библиотеки для взаимодействия с API OpenWeatherMap

owm = pyowm.OWM("f17480b84563d8c6cde6484c071ca775") 

@eel.expose #говорим что эту функцию можно использовать с js
def get_weather(place):#Описание функции с аргументом place = город который мы выбрали
	city = place #присваиваем город к переменной city
	mgr = owm.weather_manager() #присваиваем модуль api к переменной mgr
	observation = mgr.weather_at_place(city) # присваиваем mgr+погода для города
	w = observation.weather 

	temp = w.temperature('celsius')['temp']
	result = "В городе " + city + " сейчас " + str(temp) + " градусов!"
	return result

#Вывод Окна веб приложения

eel.init("web") #Создание окна веб приложения
eel.start("main.html", size=(700, 700))#исполняемый html файл для окна веб приложения