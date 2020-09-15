#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length < 2) {
  console.log('0');
} else {
  const scnd = numbers.sort(function (a, b) { return b - a; })[1];
  console.log(scnd);
}
