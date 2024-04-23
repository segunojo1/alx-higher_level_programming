#!/usr/bin/node
const { argv } = require('node:process');
function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return (1);
  } else {
    return num * factorial (num -1);
  }
}
console.log(factorial(parseInt(argv[2])));
