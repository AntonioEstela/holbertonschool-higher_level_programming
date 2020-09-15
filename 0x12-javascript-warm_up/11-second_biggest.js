#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length < 2) {
  console.log('0');
} else {
  num.sort((a, b) => { return (b - a); });
  console.log(num[1]);
}
