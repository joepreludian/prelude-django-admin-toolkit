$(() => {
    
    $('.prl-filter-select').on('change', (obj) => {
        window.location = obj.target.value;
    });

	$('select[name=action]').on('change', (obj) => {
		if (obj.target.value != '') { 
			if (confirm(gettext('Are you sure?'))) {
				$(obj.target).parents('form')[0].submit();
			}
		}
	});
	
	//https://stackoverflow.com/questions/1634748/how-can-i-delete-a-query-string-parameter-in-javascript#1634841
	function removeUrlParameter(url, parameter) {
		var urlParts = url.split('?');

		if (urlParts.length >= 2) {
			// Get first part, and remove from array
			var urlBase = urlParts.shift();

			// Join it back up
			var queryString = urlParts.join('?');

			var prefix = encodeURIComponent(parameter) + '=';
			var parts = queryString.split(/[&;]/g);

			// Reverse iteration as may be destructive
			for (var i = parts.length; i-- > 0; ) {
			// Idiom for string.startsWith
			if (parts[i].lastIndexOf(prefix, 0) !== -1) {
				parts.splice(i, 1);
				}
			}

			url = urlBase + '?' + parts.join('&');
		}

		return url;
	}
	
	function perform_search(term) {
		$('#searchbar').val(term);
		
		var search_form = $('#changelist-search');
		link = removeUrlParameter(window.location.href, 'q');
		
		search_form.prop('action', link);
		console.log(search_form.attr('action'));
		
		setTimeout(() => {
			search_form.get(0).submit();	
		}, 1000);
		
	};

	$('.prl-search').on('keypress', (evt) => {
		if (evt.which == 13) {
			perform_search(evt.target.value);
			return false;
		}
	});
	
	$('.prl-search-do').on('click', (evt) => {
		perform_search(
			$(evt.currentTarget).parent().find('input')[0].value
		);
	});
   
});