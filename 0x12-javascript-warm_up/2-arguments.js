#!/usr/bin/node

const ArgvLength = process.argv.length;

if (ArgvLength === 2) {
  console.log('No argument');
} else if (ArgvLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
