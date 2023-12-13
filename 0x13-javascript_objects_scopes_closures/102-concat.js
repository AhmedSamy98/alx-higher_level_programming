#!/usr/bin/node
const fs = require('fs');
const first = fs.readFileSync(process.argv[2], 'utf8');
const second = fs.readFileSync(process.argv[3], 'utf8');
const data = first + second;
fs.appendFileSync(process.argv[4], data);
