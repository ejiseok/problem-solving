const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString());

for (let i = 0; i < input; i++) {
  for (let j = 0; j < i + 1; j++) {
    process.stdout.write("*");
  }
  console.log();
}
