#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i = 0;
let j = 0;

while (i < size) {
  let row = '';
  j = 0;
  while (j < size) {
    row += 'X';
    j++;
  } i++;
  console.log(row);
}
