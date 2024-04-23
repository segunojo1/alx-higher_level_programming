#!/usr/bin/node
const { argv } = require('node:process');
add = function (a, b) {
  const intA = parseInt(a);
  const intB = parseInt(b);
  const sum = intA + intB;
  return (sum);
}

