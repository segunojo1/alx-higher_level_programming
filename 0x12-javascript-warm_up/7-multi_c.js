#!/usr/bin/node
const {argv} = require('node:process');

if (Number.isInteger(Number(argv[2]))) {
  const x = argv[2].parseInt();
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
