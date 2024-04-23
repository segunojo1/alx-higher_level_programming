#!/usr/bin/node
const list = require('./100-data');
console.log(list.list);
const newList = [];
list.list.map((item, index) => {
  newList.push(item * index);
  return newList;
});
console.log(newList);
