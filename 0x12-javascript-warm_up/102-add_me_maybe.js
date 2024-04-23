#!/usr/bin/node
const addMeMaybe = (x, callback) => {
  const increment = ++x;
  callback(increment);
};
module.exports = { addMeMaybe };
