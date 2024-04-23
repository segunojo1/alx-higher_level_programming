#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  const intA = parseInt(a);
  const intB = parseInt(b);
  const sum = intA + intB;
  return (sum);
}
if (!Number.isInteger(Number(argv[2])) || !Number.isInteger(Number(argv[3]))) {
  console.log('NaN');
} else {
  const sum = add(argv[2], argv[3]);
  console.log(sum);
}
