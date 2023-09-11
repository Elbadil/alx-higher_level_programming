#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const num = parseInt(argv[2]);
let lines = '';

if (isNaN(num) || argv.length < 3) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  for (let j = 0; j < num; j++) {
    lines += 'X';
  }
  console.log(lines);
  lines = '';
}
