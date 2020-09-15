#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length === 0 || numbers.length === 1) {
  console.log(0);
} else {
  let max = numbers[0];
  let scnd = numbers[0];

  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > scnd && numbers[i] !== max) {
      scnd = numbers[i];
    }
  }
  console.log(scnd);
}
