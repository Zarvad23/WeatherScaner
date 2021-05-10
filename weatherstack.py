# coding: utf-8
import requests
def weatherstack(place):
	import googletrans
	from googletrans import Translator
	params = {
	'access_key': '6053d9bf07ee6f757e1c488d39b98d13',
	'query': place
	}

	api_result = requests.get('http://api.weatherstack.com/current', params)

	api_response = api_result.json()
	time = u'%s' % (api_response['location']['localtime'])
	weather = u'%s' % (api_response['current']['weather_descriptions'][0])
	code = u'%d' % (api_response['current']['weather_code'])
	temperature = u'%d℃' % (api_response['current']['temperature'])
	feelslike = u'%d℃' % (api_response['current']['feelslike'])
	wind = u'%d' % (api_response['current']['wind_speed'])
	winddeg = u'%s' % (api_response['current']['wind_dir'])
	humidity = u'%d' % (api_response['current']['humidity'])
	precip = u'%d' % (api_response['current']['precip'])
	pressure = u'%d' % (api_response['current']['pressure'])
	cloudcover = u'%d' % (api_response['current']['cloudcover'])
	uvindex = u'%d' % (api_response['current']['uv_index'])
	visibility = u'%d' % (api_response['current']['visibility'])
	time_one = str(time[11:13])
	resultat = {
	'00':'night',
	'01':'night',
	'02':'night',
	'03':'night',
	'04':'night',
	'05':'night',
	'06':'day',
	'07':'day',
	'08':'day',
	'09':'day',
	'10':'day',
	'11':'day',
	'12':'day',
	'13':'day',
	'14':'day',
	'15':'day',
	'16':'day',
	'17':'day',
	'18':'day',
	'19':'day',
	'20':'day',
	'21':'day',
	'22':'day',
	'23':'day'
	}
	daylys = resultat[time_one]
	transs = Translator()
	pogoda = transs.translate(weather, src="en", dest="ru")
	temperature_full = "<div class='weatherstack_temperature'>" + "<div class='weatherstack_temperature_top'>" + temperature + "</div>" + "<p>" + "Ощущается" + "</p>" + "<div class='weatherstack_temperature_bottom'>" + feelslike + "</div>" + "</div>"
	weather_full = "<div class='weatherstack_weather'>" + "<img src='img/weatherstack/"+ code + "_" + daylys + ".svg'>" + "<br>" + pogoda.text + "</div>"
	wind_full = "<li>Ветер: " + wind + " км/ч " + winddeg +"</li>"
	precip_full = "<li>Осадки: " + precip + " мм</li>"
	pressure_full = "<li>Давление: " + pressure + " млбар</li>"
	humidity_full = "<li>Влажность: " + humidity + "%</li>"
	cloudcover_full = "<li>Облачность: " + cloudcover + "ок</li>"
	uvindex_full = "<li>UV Индекс: " + uvindex + "</li>"
	visibility_full = "<li>Видимость: " + visibility + " км</li>"
	details = "<div class='weatherstack_details'>" +"<ul>" + wind_full + precip_full + pressure_full + humidity_full + cloudcover_full + uvindex_full + visibility_full + "</ul>" + "</div>"
	result = "<div class='weathestack_container'>"+ weather_full + temperature_full + details +"</div>"
	return result
