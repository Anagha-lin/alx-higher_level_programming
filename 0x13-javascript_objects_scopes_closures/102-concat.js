#!/usr/bin/node

const fs = require('fs');

// Extract file paths from command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read the content of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read the content of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate the content of fileA and fileB
    const concatenatedData = dataA + '\n' + dataB;

    // Write the concatenated data to fileC
    fs.writeFile(fileC, concatenatedData, (err) => {
      if (err) throw err;
      console.log(`${fileA} and ${fileB} were successfully concatenated and written to ${fileC}`);
    });
  });
});

