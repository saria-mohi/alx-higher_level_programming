#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

// read data from file or print error if not exist
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
