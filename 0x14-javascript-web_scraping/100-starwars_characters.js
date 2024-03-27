#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  // Function to get character names from URLs
  const getCharacterNames = (urls) => {
    const promises = urls.map(url =>
      new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          if (response.statusCode !== 200) {
            reject(`Error: Status code ${response.statusCode}`);
            return;
          }
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      })
    );
    return Promise.all(promises);
  };

  // Retrieve character names and print them
  getCharacterNames(charactersUrls)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});

