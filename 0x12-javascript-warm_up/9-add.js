#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(argv[2], argv[3]));
