#!/usr/bin/node

exports.callMeMoby = function(a, operation) {
	let i = 0;

	while (i < a) {
		operation();
		i++;
	}
}
