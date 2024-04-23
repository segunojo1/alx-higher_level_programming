#!/usr/bin/node
const callMeMoby = (x, callback) => {
  for(let i = 0; i < x; i++) {
    callback();
  }
}
module.exports = { callMeMoby };
