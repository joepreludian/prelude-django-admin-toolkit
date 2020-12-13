$(() => {
    
    $('.prl-filter-select').on('change', (obj) => {
        window.location = obj.target.value;
    });

	$('select[name=action]').on('change', (obj) => {
		if (confirm(gettext('Are you sure?'))) {
			if (obj.target.value != '') { 
				$(obj.target).parents('form')[0].submit();
			}
		}
	});
   
});
