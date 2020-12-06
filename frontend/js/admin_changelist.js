$(() => {
    
    $('.prl-filter-select').change('change', (obj) => {
        window.location = obj.target.value;
    });
   
});
