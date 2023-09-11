#!/usr/bin/node

const process = require('process');
const argv = process.argv;
let num = parseInt(argv[2]);

if (isNaN(num) || argv.length < 3) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log('C is fun');
  num -= 1;
}
