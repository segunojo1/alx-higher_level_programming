#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (number) {
    if (number < base) {
      return number.toString();
    } else {
      return convertToBase(Math.floor(number / base)) + (number % base).toString();
    }
  };
};
