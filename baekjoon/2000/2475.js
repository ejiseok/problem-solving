const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((num) => Number(num));

sum = input.reduce((num1, num2) => num1 + num2 * num2, 0);

console.log(sum % 10);
