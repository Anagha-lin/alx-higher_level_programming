#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
  constructor(size) {
    super(size); // Call the constructor of the Square class
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X'; // Set default character to 'X' if c is undefined
    }
    const row = c.repeat(this.width); // Create a row of characters
    for (let i = 0; i < this.height; i++) {
      console.log(row); // Print the row 'height' times
    }
  }
}

module.exports = SquareWithCharPrint;

