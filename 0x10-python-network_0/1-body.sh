#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response

curl -s -X GET "$1" -o /tmp/response.txt
if [ "$(grep -c '^HTTP/1.1 200 OK' /tmp/response.txt)" -eq 1 ]; then
    awk '/^\r?$/{flag=1;next}flag' /tmp/response.txt
fi

