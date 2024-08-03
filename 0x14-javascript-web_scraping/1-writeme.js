#!/usr/bin/node

/*
script that writes content
to a file
*/

const fs = require('fs');
/*
file path
*/
const filePath = process.argv[2];
/*
content to write
*/
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
