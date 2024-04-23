!#/usr/bin/node
const { argv } = require(node:process);
function factorial (num) {
  if (num === 0 || num === 1 || isNan(num)) {
    return (1);
  } else {
    return num * factorial (num -1);
  }
}
factorial(parseInt(argv[2]);
