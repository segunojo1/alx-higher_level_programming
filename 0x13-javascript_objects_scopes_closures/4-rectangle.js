#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const tempw = this.width;
    this.width = this.height;
    this.height = tempw;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}
module.exports = Rectangle;
