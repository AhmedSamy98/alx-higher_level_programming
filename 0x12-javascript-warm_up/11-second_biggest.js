#!/usr/bin/node

const length = process.argv.length;
const allArguments = process.argv.slice(2);
const integers = allArguments.map(arg => parseInt(arg));

function largest (array) {
  let largestNum = array[0];
  let i = 0;

  while (i < array.length) {
    if (array[i] > largestNum) {
      largestNum = array[i];
    }
    i++;
  }
  return largestNum;
}

if (length < 2) {
  console.log('0');
} else {
  const largestnum = largest(integers);
  const indexOfLargest = integers.indexOf(largestnum);
  integers.splice(indexOfLargest, 1);
  const secondLargestNum = largest(integers);
  console.log(secondLargestNum);
}
