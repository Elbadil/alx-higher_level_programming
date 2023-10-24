#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const request = require('request');

const MovieID = argv[2];
const MovieURL = `https://swapi-api.alx-tools.com/api/films/${MovieID}`;

request(MovieURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
