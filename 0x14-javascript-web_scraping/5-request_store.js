#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, resp, body) => {
  if (err) throw err;
  fs.writeFile(path, body, error => {
    if (error) throw error;
  });
});
