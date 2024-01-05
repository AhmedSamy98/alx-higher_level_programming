#!/bin/bash
# a Bash script that sends a POST request with 2 variables
curl -s -L -X POST "$1" -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD"
