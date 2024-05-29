#!/usr/bin/node
const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/:id';

//  first argument is the episode ID
const episodeId = process.argv[2];

request(`${baseUrl}/${episodeId}/`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
