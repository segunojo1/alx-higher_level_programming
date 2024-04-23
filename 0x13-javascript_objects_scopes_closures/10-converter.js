#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase(number) {
    return number < base ? String(number) : convertToBase(number / base | 0) + String(number % base);
  };
};
