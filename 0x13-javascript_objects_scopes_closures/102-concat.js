#!/usr/bin/node
let A = process.argv[2];
let B = process.argv[3];
let C = process.argv[4];
let fs = require('fs');
let textA = fs.readFileSync(A, 'utf8');
let textB = fs.readFileSync(B, 'utf8');
fs.writeFileSync(C, textA + textB);
