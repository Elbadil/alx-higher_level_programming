#!/bin/bash
# Bash script that sends A POST request to the passed URL and adds variables to be sent
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" 
