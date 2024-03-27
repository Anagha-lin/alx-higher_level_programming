#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles' character ID

// Function to count movies where the character is present
function countMoviesWithCharacter(apiUrl, characterId) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Status code ${response.statusCode}`);
      return;
    }

    const filmsData = JSON.parse(body).results;
    const moviesWithCharacter = filmsData.filter(film =>
      film.characters.some(character => character.endsWith(`/${characterId}/`))
    );

    console.log(moviesWithCharacter.length);
  });
}

// Call the function
countMoviesWithCharacter(apiUrl, characterId);

