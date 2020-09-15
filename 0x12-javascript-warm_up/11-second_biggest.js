#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length === 0 || numbers.length === 1) {
  console.log(0);
} else {
  numbers.sort().reverse();
  console.log(numbers[1]);
}
