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
	
	function perform_search(term) {
		$('#searchbar').val(term);
		$('#changelist-search').get(0).submit();	
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