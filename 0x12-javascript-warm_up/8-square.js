#!/usr/bin/node
const {argv} = require('node:process');

if (Number.isInteger(Number(argv[2]))) {
  const x = argv[2].parseInt();
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      console.log('X');
    }
  }
} else {
  console.log('Missing size');
}
