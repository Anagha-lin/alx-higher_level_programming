#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Extract command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request and pipe response to file
request(url)
  .on('error', (error) => {
    console.error(error);
  })
  .pipe(fs.createWriteStream(filePath, { encoding: 'utf-8' }))
  .on('finish', () => {
    console.log(`Successfully saved the contents of ${url} to ${filePath}`);
  });

