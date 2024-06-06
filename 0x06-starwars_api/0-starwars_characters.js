#!/usr/bin/node
/* Get the actors name */

const request = require('request');

const args = process.argv;

if (args.length !== 3) {
  process.exit(1);
}

const id = args[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
      const chars = JSON.parse(body).characters;
      getChars(chars, 0);
  }
});

function getChars(chars, index) {
  request(chars[index], (err, res, body) => {
      if (err) {
          console.log(err);
      } else {
          console.log(JSON.parse(body).name);
          if (index + 1 < chars.length) {
              getChars(chars, index + 1);
          }
      }
  });
}
