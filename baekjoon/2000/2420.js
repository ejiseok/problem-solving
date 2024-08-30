const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let n = parseInt(input[0]);
let m = parseInt(input[1]);

console.log(Math.abs(n - m));
