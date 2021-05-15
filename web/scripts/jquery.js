jQuery('#show').on('click', function(){//для удобства чтобы при нажатии кнопки запускался скрипт
	display_weather();
	$('#gorod').show( "slow");
	$('#reload').show( "slow");
	var iconcode = a.weather['10d'].icon;
	var iconurl = "http://openweathermap.org/img/w/" + iconcode + ".png";
	$('#wicon').attr('src', iconurl);
})