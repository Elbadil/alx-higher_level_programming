#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const request = require('request');
const fs = require('fs');

const URL = argv[2];
const filename = argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const fileContent = body;
    fs.writeFile(filename, fileContent, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
