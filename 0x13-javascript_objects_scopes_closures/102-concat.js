#!/usr/bin/node
const fs = require('fs');
const [, , file1Path, file2Path, destinationPath] = process.argv;

fs.readFile(file1Path, 'utf8', (err, data1) => {
  if (err) throw err;
  fs.readFile(file2Path, 'utf8', (err, data2) => {
    if (err) throw err;
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
