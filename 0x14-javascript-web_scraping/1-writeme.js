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
let content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
