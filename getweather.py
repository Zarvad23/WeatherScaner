import pyowm #подключение библиотеки для взаимодействия с API OpenWeatherMap
import math
from pyowm.utils.config import get_default_config	

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = pyowm.OWM("f17480b84563d8c6cde6484c071ca775") 

def get_weather(place):
	city = place #присваиваем город к переменной city
	mgr = owm.weather_manager() #присваиваем модуль api к переменной mgr
	observation = mgr.weather_at_place(city) # присваиваем mgr+погода для города
	w = observation.weather 

	temp = math.ceil(w.temperature('celsius')['temp'])
	temp_feel = math.ceil(w.temperature('celsius').get('feels_like', None))
	details = w.detailed_status
	icon = w.weather_icon_url(size='2x')
	result1 = "<li>" + "<span>" + details + "</span>" + "<div class='right'>" + "<img src=" + icon +" >" + "<div>" + "<p>" +str(temp)+ "℃" + "</p>" +"<p id='feels_like'>" + "Ощущается:" + "</p>" + "<p>" +str(temp_feel)+ "℃" + "</p>" + "</div>" + "</div>" + "</li>"

	wind = w.wind()['speed']
	winddeg = w.wind()['deg']
	humidity = w.humidity
	humidity_full = "<div>" + "<img src='img/humidity.svg' class='icon-wind-direction'>" + "Влажность: " + str(humidity) + "%" + "</div>"
	result2 = "<li>" + "<div>" + "<svg data-v-47880d39='' viewBox='0 0 1000 1000' enable-background='new 0 0 1000 1000' xml:space='preserve' class='icon-wind-direction' style='transform: rotate("+str(winddeg)+"deg);'>"+"<g data-v-47880d39='' fill='#48484a'>"+"<path data-v-47880d39='' d='M510.5,749.6c-14.9-9.9-38.1-9.9-53.1,1.7l-262,207.3c-14.9,11.6-21.6,6.6-14.9-11.6L474,48.1c5-16.6,14.9-18.2,21.6,0l325,898.7c6.6,16.6-1.7,23.2-14.9,11.6L510.5,749.6z'>"+"</path><path data-v-47880d39='' d='M817.2,990c-8.3,0-16.6-3.3-26.5-9.9L497.2,769.5c-5-3.3-18.2-3.3-23.2,0L210.3,976.7c-19.9,16.6-41.5,14.9-51.4,0c-6.6-9.9-8.3-21.6-3.3-38.1L449.1,39.8C459,13.3,477.3,10,483.9,10c6.6,0,24.9,3.3,34.8,29.8l325,898.7c5,14.9,5,28.2-1.7,38.1C837.1,985,827.2,990,817.2,990z M485.6,716.4c14.9,0,28.2,5,39.8,11.6l255.4,182.4L485.6,92.9l-267,814.2l223.9-177.4C454.1,721.4,469,716.4,485.6,716.4z'>"+"</path></g></svg>" + "Ветер: " + str(wind) + " м/с" + "</div>" + humidity_full + "</li>"
	visibilit = w.visibility() / 1000
	visibilit_full = "<div>" + "<img src='img/visibility.svg' class='icon-wind-direction'>" + "Видимость: " + str(visibilit) + "км" + "</div>"
	pressur = w.pressure['press']
	result3 = "<li>" + "<div>" + "<img src='img/gauge.svg' class='icon-wind-direction'>" + "Давление: " + str(pressur) + "hPa" + "</div>" + visibilit_full + "</li>"
	result = "<ul>"+result1+result2+result3+"</ul>"
	return result