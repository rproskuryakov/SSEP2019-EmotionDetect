const config = {
	imageLoading: 'static/images/loading.svg',
	imageError: 'static/images/error.svg',
	imagePositive: 'static/images/positive.svg',
	imageNegative: 'static/images/negative.svg',
	apiAddress: 'http://127.0.0.1:5000/prediction',
	apiParam: 'api parammmmmmmmmmm'
}
const elem = {
	text: document.getElementById("form-text"),
	resultImage: document.getElementById("result-image"),
	resultText: document.getElementById("result-text")
}
var scrolling = false;

$(document).ready(function(){
	$('.carousel').slick({
		dots: true,
		autoplay: true,
		autoplaySpeed: 4000
	});
})

function sendForm() {
	let text = elem.text.value;

	var obj = {}
	obj[config.apiParam] = text;

	$.ajax(config.apiAddress, {
		method: 'POST',
		data: obj
	}).done(function(data) {
		console.log(data);
		if(data === "0")
			showResult(0, "Негативный");
		else if(data === "1")
			showResult(1, "Позитивный");
		else
			showResult(-2, "Неизвестный результат!");
	}).fail(function() {
		console.log("fail");
		showResult(-2, "Ошибка!");
	});

	showResult(-1, "Загрузка...");
}
function showResult(result, message) {
	switch(result) {
		case -1:
			elem.resultImage.src = config.imageLoading;
			break;
		case 0:
			elem.resultImage.src = config.imageNegative;
			break;
		case 1:
			elem.resultImage.src = config.imagePositive;
			break;
		default:
			elem.resultImage.src = config.imageError;
	}
	elem.resultText.innerText = message;
}
function scrollToAnchor(anchor) {
	var offset = $("#" + anchor).offset().top;
	$('body').animate({
		scrollTop: offset
	}, 500);
}
