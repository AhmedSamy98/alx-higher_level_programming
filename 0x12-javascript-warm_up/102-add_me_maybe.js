#!/usr/bin/node

exports.addMeMaybe = function(a, operation) {
	operation(++a);
}
