#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;

request(url, (error, body) => {
  if (error) throw error;
  const response = JSON.parse(body.toJSON().body);
  console.log(response.title);
});
