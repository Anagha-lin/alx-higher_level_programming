$(document).ready(function(){
    // Make an HTTP GET request to fetch movie data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: function(data) {
            // Iterate through the list of movies and append each title to the list
            $.each(data.results, function(index, movie) {
                $('<li>').text(movie.title).appendTo('#list_movies');
            });
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error('Error:', error);
        }
    });
});

