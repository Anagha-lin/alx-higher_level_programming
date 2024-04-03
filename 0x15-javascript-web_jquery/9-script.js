$(document).ready(function(){
    // Make an HTTP GET request to fetch the translation of "hello"
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            // Update the content of the <div id="hello">
            $('#hello').text(data.hello);
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error('Error:', error);
        }
    });
});

