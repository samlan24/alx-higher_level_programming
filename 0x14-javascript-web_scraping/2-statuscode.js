#!/usr/bin/node

/*
script that writes code status  
*/

const { STATUS_CODES } = require('http');
const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
