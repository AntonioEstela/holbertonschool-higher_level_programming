#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  for (const film in films) {
    const characters = films[film].characters;
    if (characters.includes(character)) {
      count++;
    }
  }
  console.log(count);
});
