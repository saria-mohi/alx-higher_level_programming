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
<<<<<<< HEAD
});
=======
});
>>>>>>> 1c163d494b10087e5793a992432e02c191fe48b7
