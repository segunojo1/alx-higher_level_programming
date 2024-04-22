#!/usr/bin/node
const {argv} = require('node:process');
if(argv[3]) {
    console.log(argv[3]);
} else {
    console.log('No argument');
}
