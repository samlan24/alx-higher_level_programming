#!/usr/bin/node

/*
script that reads and prints
content of a file
*/

const fs = require('fs');
/*
file path
*/

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
