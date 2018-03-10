$(document).ready( function() {
	var time = 10;
	var interval;
	var announce;
	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

	$(".link").click(function(e){
		console.log(e.target.textContent);
		console.log('post route');
		$.ajax({
			url: '/guide',
			type: 'POST',
			headers: {'X-CSRFToken': '{{ csrf_token }}'},
			data: e.target.textContent,
			success: function(data){
				window.location.href = '/guide'
			},
			error: function(err){
				console.log(err)
			}
		});
	});

	announce = $("#announce").text()
	$("#announce").html(announce)

	interval = setInterval(tick, 1000);

	function tick(){
		$("#timer").html(time);
		time -= 1;
		if(time <= 0){
			clearInterval(interval);
			$("#announce").html("Time's Up!");
			$("#guessform").prop("disabled", true);
		}
	}

	$("#synonym").click(function(){
		window.location.href = '/index'
	})

});
