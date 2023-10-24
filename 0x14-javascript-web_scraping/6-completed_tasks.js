#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const request = require('request');

const todosURL = argv[2];

request(todosURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const usersTasks = {};
    const todosData = JSON.parse(body);
    todosData.forEach((item) => {
      if (item.completed === true) {
        const usersID = item.userId;
        if (!(usersID in usersTasks)) {
          usersTasks[usersID] = 0;
        }
        usersTasks[usersID] += 1;
      }
    });
    console.log(usersTasks);
  }
});
