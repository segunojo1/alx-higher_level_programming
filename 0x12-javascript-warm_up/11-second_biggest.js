#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2, len);
  const sortedArgs = args.sort((a, b) => a - b);
  console.log(sortedArgs[len - 2]);
}
