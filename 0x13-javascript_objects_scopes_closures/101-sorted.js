#!/usr/bin/node
const { dict } = require('./101-data');

const usersByOccurrences = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!usersByOccurrences[occurrences]) {
    usersByOccurrences[occurrences] = [];
  }
  usersByOccurrences[occurrences].push(parseInt(userId));
}

console.log(usersByOccurrences);
