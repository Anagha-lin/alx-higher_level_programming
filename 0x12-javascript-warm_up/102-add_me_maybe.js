#!/usr/bin/node

function addMeMaybe(number, theFunction) {
  const newValue = number + 1;
  theFunction(newValue);
}

module.exports.addMeMaybe = addMeMaybe;

