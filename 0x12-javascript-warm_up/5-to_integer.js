#!/usr/bin/node

const process = require('process');

const argv = process.argv;

const num = parseInt(argv[2]);

if (isNaN(num) || argv.length < 3) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
