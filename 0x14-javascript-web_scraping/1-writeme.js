#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

// Write content to file
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    // Print error object if an error occurs
    console.error(error);
  }
});

