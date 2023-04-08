import { open } from 'node:fs/promises';

const file = await open('data.txt');
let testArr = [];
let sumArr = [];
let sum = 0

for await (const line of file.readLines()) {
  testArr.push(Number(line));
}

for (let i in testArr){
  if (testArr[i] != 0){
    sum += testArr[i]
  } else {
    sumArr.push(sum)
    sum = 0;
  }
}
sumArr.sort((a, b) => b - a);
let topElf = sumArr[0]
let topThree = sumArr[0] + sumArr[1] + sumArr[2];
console.log(`The elf with the most calories is ${topElf}`)
console.log(`\nThe total of calories from the top three elves \ncombined is ${topThree}`)
  