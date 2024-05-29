#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// file path
const file = process.argv[2];
// string to write
const text = process.argv[3];
// write in utf-8
fs.writeFile(file, text, 'utf8', function (err, data) {
  // print the error object
  if (err) {
    console.log(err);
  }
});
