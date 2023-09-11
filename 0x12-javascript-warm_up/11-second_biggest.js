#!/usr/bin/node

const process = require('process');
const argv = process.argv;

let largestNum = -Infinity;
let secondLarge = -Infinity;

if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > largestNum) {
      largestNum = parseInt(argv[i]);
    }
  }

  for (let j = 2; j < argv.length; j++) {
    if (parseInt(argv[j]) > secondLarge && parseInt(argv[j]) !== largestNum) {
      secondLarge = parseInt(argv[j]);
    }
  }

  console.log(secondLarge);
}
