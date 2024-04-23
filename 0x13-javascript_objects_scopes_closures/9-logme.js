#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  counter++;
  myFunction(counter, item);
};

function myFunction (count, item) {
  console.log(count, ': ', item);
}
