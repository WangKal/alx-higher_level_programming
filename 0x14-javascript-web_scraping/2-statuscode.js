#!/usr/bin/node
const process = require('process');
const request = require('request');

//  request url
const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    // display the status code
    console.log(`code: ${response.statusCode}`);
  }
});
