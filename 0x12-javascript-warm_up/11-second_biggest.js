#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length < 2) {
  console.log('0');
} else {
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
