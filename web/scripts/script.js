	async function display_weather(){
			let place = document.getElementById('location').value;//Получаем из текстового поля стринг значение
			document.getElementById('gorod').innerHTML = place;//полученное значение выводим в див с id info
			let res = await eel.main(place)();//отдаем pythom значение place на обработку
			let res2 = await eel.two(place)();
			let res3 = await eel.yahoo(place)();
			document.getElementById('yahoo').innerHTML = res3;
			document.getElementById('output').innerHTML = res2;//полученное значение выводим в див с id info
			document.getElementById('info').innerHTML = res;//полученное значение выводим в див с id info
		}

		$('.tabs-wrapper').each(function() {
			let ths = $(this);
			ths.find('.tab-item').not(':first').hide();
			ths.find('.tab').click(function() {
				ths.find('.tab').removeClass('active').eq($(this).index()).addClass('active');
				ths.find('.tab-item').hide().eq($(this).index()).fadeIn()
			}).eq(0).addClass('active');
		});