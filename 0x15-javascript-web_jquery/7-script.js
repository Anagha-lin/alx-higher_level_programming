$(document).ready(function(){
    // Make an HTTP GET request to fetch character data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(data) {
            // Update the text content of the <div id="character">
            $('#character').text(data.name);
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error('Error:', error);
        }
    });
});

