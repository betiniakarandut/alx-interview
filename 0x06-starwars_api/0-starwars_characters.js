#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi.dev/api';

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const fetchCharacterName = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, _, characterBody) => {
      if (error) {
        reject(error);
        return;
      }
      const character = JSON.parse(characterBody);
      resolve(character.name);
    });
  });
};

request(`${API_URL}/films/${movieId}/`, async (err, _, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const charactersURL = film.characters;

  try {
    const characterNames = await Promise.all(charactersURL.map(fetchCharacterName));
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    console.error(error);
  }
});
