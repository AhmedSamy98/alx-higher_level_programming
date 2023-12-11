#!/usr/bin/node

const myInt = parseInt(process.argv[2]);

if (!isNaN(myInt)) {
  console.log('My number:', process.argv[2]);
} else {
  console.log('Not a number');
}
