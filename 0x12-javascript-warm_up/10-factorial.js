#!/usr/bin/node
function factorial (n) {
	if (n === || n === 1) {
		return 1;
	} else if (n) {
		return factorial(n - 1) * n;
	}
	return 1;
}
let n = parseInt(process.argv[2]);
console.log(factorial(n));
