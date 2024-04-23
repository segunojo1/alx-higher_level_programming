#!/usr/bin/node
const addMeMaybe = (x, callback) => {
  x++;
  callback();
};
module.exports = { addMeMaybe };
