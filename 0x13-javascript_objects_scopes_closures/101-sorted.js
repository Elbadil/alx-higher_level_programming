#!/usr/bin/node

const dict = require('./101-data').dict;

const newDictionay = {};

for (const key in dict) {
  if (!newDictionay[dict[key]]) {
    newDictionay[dict[key]] = [key];
  } else {
    newDictionay[dict[key]].push(key);
  }
}
console.log(newDictionay);
