#!/usr/bin/node
const { argv } = require('node:process');
const argv0 = argv[2];
if (Number.isInteger(Number(argv[2]))) {
  console.log('My number: ', argv0);
} else {
  console.log('Not a number');
}
