$(document).ready(function() {
	$('#sub').on('click', function(e) {
		if($('#a').val() && $('#b').val() && $('#c').val())
		{
			e.preventDefault();
			var form = document.getElementById('data-form');
			var data = new FormData(form);

			$.ajax({
				url: '/',
				method: 'POST',
				data: data,
				processData: false,
				contentType: false
			}).then(function(data) {
				/** @namespace data.msg */
				$('#result').html(data.msg);
			}, function(xhr) {
				/** @namespace xhr.responseJSON */
				$('#result').text(xhr.responseJSON.msg);
			});
		}
	})
});