$(function(){
	$('button').click(function(){
		var user = $('#term').val();
		var pass = $('#start_date_field').val();
		$.ajax({
			url: '/http://api.nytimes.com/svc/search/v2/articlesearch.json',
			data: $('form').serialize(),
			type: 'GET',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});