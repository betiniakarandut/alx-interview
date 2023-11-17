#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const charactersURL = film.characters;

  const printCharacterNames = (characterUrls) => {
    characterUrls.forEach((url) => {
      request(url, (error, _, characterBody) => {
        if (error) {
          console.error(error);
          return;
        }
        const character = JSON.parse(characterBody);
        console.log(character.name);
      });
    });
  };

  printCharacterNames(charactersURL);
});
