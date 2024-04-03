$(document).ready(function(){
    // Add click event listener to DIV#add_item
    $('#add_item').click(function(){
        // Append a new <li> element to the <ul> with class 'my_list'
        $('<li>Item</li>').appendTo('.my_list');
    });
});

