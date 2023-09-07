#!/usr/bin/node

const request = require('request');
const process = require('process');

function getCharactersInMovie(movieId) {
  // Construct the URL for the SWAPI film endpoint with the provided movieId
  const url = `https://swapi.dev/api/films/${movieId}/`;

  // Make a GET request to the SWAPI
  request(url, { json: true }, (error, response, filmData) => {
    if (error) {
      console.error(`Failed to retrieve film data for movie ID ${movieId}`);
      return;
    }

    if (response.statusCode === 200 && filmData) {
      const characterUrls = filmData.characters;

      // Function to fetch character data and print names
      function fetchCharacterData(characterUrl) {
        request(characterUrl, { json: true }, (charError, charResponse, charData) => {
          if (charError) {
            console.error(`Failed to retrieve character data for ${characterUrl}`);
            return;
          }

          if (charResponse.statusCode === 200 && charData) {
            console.log(charData.name);
          } else {
            console.error(`Failed to retrieve character data for ${characterUrl}`);
          }
        });
      }

      // Iterate through character URLs and fetch data
      characterUrls.forEach((characterUrl) => {
        fetchCharacterData(characterUrl);
      });
    } else {
      console.error(`Failed to retrieve film data for movie ID ${movieId}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: script_name.js movie_id');
  process.exit(1);
}

const movieId = process.argv[2];
getCharactersInMovie(movieId);
