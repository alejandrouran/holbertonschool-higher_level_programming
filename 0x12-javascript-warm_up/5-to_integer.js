#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (parsed) {
  console.log('My number: ' + parsed);
} else {
  console.log('Not a number');
}
