#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const epi_id = process.argv[2];
const api_url = 'https://swapi-api.hbtn.io/api/films/';

request(api_url + epi_id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});