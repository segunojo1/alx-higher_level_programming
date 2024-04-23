#!/usr/bin/node
const addMeMaybe = (x, callback) => {
  callback(++x);
};
module.exports = { addMeMaybe };
