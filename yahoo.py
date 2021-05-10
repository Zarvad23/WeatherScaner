from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit



def yahoo_weather (place):
	import googletrans
	from googletrans import Translator
	data = YahooWeather(APP_ID="2omyTeoj",
		api_key="dj0yJmk9cEFHakg3UXlpZ056JmQ9WVdrOU1tOXRlVlJsYjJvbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTk3",
		api_secret="f1791a176acc6c5f52b6c6cae7e6cd4b5fb82068")

	data.get_yahoo_weather_by_city(place, Unit.celsius)
	transs = Translator()
	pogoda = transs.translate(str(data.condition.text), src="en", dest="ru")
	code = (data.condition.code)
	direction = (data.wind.direction) #направление ветра для иконки
	weather_desc = "<li>" + "<div class ='clouds_title'>" + "<img src=" + r"img/monoflat/" + str(code) + ".png" + " >" + pogoda.text + "</div>" + "</li>"
	temperature = "<li>" + str(data.condition.temperature) + "℃" + "</li>"
	feels_like = "<div> Ощущается: " + str(data.wind.chill) + "℃</div>"
	wind_speed = "<div> Ветер: " + "<br>" + str(data.wind.speed) + "м/с</div>"
	humidity = "<div> Влажность: " + str(data.atmosphere.humidity) + "%</div>"
	visibility = "<div> Видимость: " + str(data.atmosphere.visibility) + " км</div>"
	pressure = "<div> Барометр: " + "<br>" + str(data.atmosphere.pressure) + " millibars</div>"
	Windmill = "<div>" + "<img src='img/Windmill.png'>" + "</div>"
	wind_pressure = "<div class='container_2'>" + "<p>" + "Ветер & Давление" + "</p>" + "<div class='wind_detaild'>" + Windmill + wind_speed + pressure + "</div>" + "</div>"
	details = "<li>"+ "<div class='container'>" + "<p>" + "Детали" + "</p>" + "<div class='details_container'>" + "<div class='details_image'>" + "<img src=" + r"img/monoflat/" + str(code) + ".png" + " >" + "</div>" + "<div class='details'>" + feels_like + humidity + visibility + "</div>" + "</div>" + wind_pressure + "</div>" + "</li>"
	

	result = "<ul>" + weather_desc + temperature + details + "</ul>"
	return result
