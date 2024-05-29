#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// request url
const baseURL = process.argv[2];
// file path to store the body response
const bodyResp = process.argv[3];
request(baseURL, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(bodyResp, body);
  }
});
