#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const argv = process.argv;

fs.readFile(argv[2], 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
