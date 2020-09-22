#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';
const character = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, body) => {
  if (error) throw error;
  const response = JSON.parse(body.toJSON().body);
  const films = response.results;
  let count = 0;

  for (const film in films) {
    const characters = films[film].characters;
    if (characters.includes(character)) {
      count++;
    }
  }
  console.log(count);
});
