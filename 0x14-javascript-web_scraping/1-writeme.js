#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const argv = process.argv;

const filename = argv[2];
const content = argv[3];
fs.writeFile(filename, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
