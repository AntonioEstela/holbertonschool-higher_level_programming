#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films';

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  for (const film of films) {
    for (const characters of film.characters) {
      if (characters.includes('18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
