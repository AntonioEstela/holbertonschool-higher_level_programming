#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    for (const film of data.results) {
      for (const char of film.characters)
        if (char.endsWith('18/')) {
          count++;
        }
    }
    console.log(count);
  }
});
