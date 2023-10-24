#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const request = require('request');

const WedgeAntillesID = "/18/";
const filmsURL = argv[2];

request(filmsURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let counter = 0;
    const filmsData = JSON.parse(body);
    for (const film of filmsData.results) {
      for (const character of film.characters) {
        if (character.endsWith(WedgeAntillesID)) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
