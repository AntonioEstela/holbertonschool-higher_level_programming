#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 0 || number === 1) {
    return 1;
  } else {
    return factorial(number - 1) * number;
  }
}

const number = Number(process.argv[2]);

console.log(factorial(number));
