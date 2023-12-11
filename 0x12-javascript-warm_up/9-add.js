#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(`${result}`);
}

add(a, b);
