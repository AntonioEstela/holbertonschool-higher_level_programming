#!/usr/bin/node
const args = process.argv.slice(2);

if (args[0] !== undefined && args[1] === undefined) {
  console.log('Argument found');
} else if (args[1] !== undefined) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
