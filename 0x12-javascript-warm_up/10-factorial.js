#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

console.log(factorial(argv[2]));
