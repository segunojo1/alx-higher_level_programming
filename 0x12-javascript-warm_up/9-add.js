#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(parseInt(argv[2]), parseInt(argv[3]));
