#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) throw err;

  const data = {};
  const todo = JSON.parse(body);

  for (let i = 0; i < todo.length; i++) {
    const userId = todo[i].userId;
    const taskStatus = todo[i].completed;

    if (taskStatus === true) {
      if (!data[userId]) {
        data[userId] = 1;
      } else {
        data[userId] += 1;
      }
    }
  }
  console.log(data);
});
