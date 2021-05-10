import eel #подключение библиотеки веб интерфесов
from getweather import get_weather
from weatherstack import weatherstack
from yahoo import yahoo_weather
from translate import translate


@eel.expose #говорим что эту функцию можно использовать с js
def main(place):#Описание функции с аргументом place = город который мы выбрали
	translate(place)
	overlay = get_weather(place)
	return overlay

@eel.expose
def two(place):
	weat = weatherstack(place)
	return weat

@eel.expose
def yahoo(place):
	weat = yahoo_weather(place)
	return weat
#Вывод Окна веб приложения

eel.init("web") #Создание окна веб приложения
eel.start("main.html", size=(700, 700))#исполняемый html файл для окна веб приложения