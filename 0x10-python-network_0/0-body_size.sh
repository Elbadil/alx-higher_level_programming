#!/bin/bash
# Bash script that displays the size of the body of an HTTP response

curl -Is $1 | grep -i "Content-Length" | awk '{print $2}'
