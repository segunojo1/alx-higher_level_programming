#!/usr/bin/node
const { argv } = require('node:process');
if (Number.isInteger(Number(argv[2]))) {
  const x = parseInt(argv[2]);
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
