#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// file path
const file = process.argv[2];
//Write content  in utf-8
fs.readFile(file, 'utf8', function (err, data) {
  // Print the error if it occurs
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
