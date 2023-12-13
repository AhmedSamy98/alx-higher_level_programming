#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const elements = list.filter(item => item === searchElement);
  return elements.length;
};
