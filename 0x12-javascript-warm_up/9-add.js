#!/usr/bin/node
const {argv} = require('node:process')
function add(a, b) {
  let sum = a + b;
  return (sum);
}
if (!Number.isInteger(Number(argv[2])) || !Number.isInteger(Number(argv[3]))) {
  console.log('Nan');
} else {
  const sum = add(argv[2] + argv[3]);
  console.log( sum);
}
