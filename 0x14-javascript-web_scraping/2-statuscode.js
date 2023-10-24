#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const request = require('request')

const URL = argv[2];
request(URL, (error, response, body) => {
  console.log(response.statusCode);
});
