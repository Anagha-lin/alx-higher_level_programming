$(document).ready(function(){
    // Add click event listener to DIV#toggle_header
    $('#toggle_header').click(function(){
        // Toggle classes 'red' and 'green' on the <header> element
        $('header').toggleClass('red green');
    });
});

