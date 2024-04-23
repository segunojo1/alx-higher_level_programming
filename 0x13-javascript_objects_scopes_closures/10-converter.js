#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (number) {
    const digits = '0123456789abcdef';
    if (number < base) {
      return digits[number];
    } else {
      return convertToBase(Math.floor(number / base)) + digits[number % base];
    }
  };
};
