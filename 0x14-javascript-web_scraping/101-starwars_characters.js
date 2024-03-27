#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch movie details
function getMovieDetails(movieId) {
  return new Promise((resolve, reject) => {
    request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode !== 200) {
        reject(`Error: Status code ${response.statusCode}`);
      }
      resolve(JSON.parse(body));
    });
  });
}

// Function to fetch character details
function getCharacterDetails(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode !== 200) {
        reject(`Error: Status code ${response.statusCode}`);
      }
      resolve(JSON.parse(body).name);
    });
  });
}

// Function to print character names
async function printCharacterNames(movieId) {
  try {
    const movieDetails = await getMovieDetails(movieId);
    const characters = movieDetails.characters;
    
    for (const characterUrl of characters) {
      const characterName = await getCharacterDetails(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
}

// Call the function to print character names
printCharacterNames(movieId);

