#!/usr/bin/node

function secondBiggest(numbers) {
    if (numbers.length <= 1) {
        return 0;
    }

    let max = -Infinity;
    let secondMax = -Infinity;

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > max) {
            secondMax = max;
            max = numbers[i];
        } else if (numbers[i] > secondMax && numbers[i] < max) {
            secondMax = numbers[i];
        }
    }

    return secondMax;
}

const args = process.argv.slice(2).map(Number);
console.log(secondBiggest(args));

