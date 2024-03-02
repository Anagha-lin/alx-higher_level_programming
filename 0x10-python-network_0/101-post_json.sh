#!/bin/bash
# This script sends a JSON POST request to the URL passed as the first argument, with the contents of a file passed as the second argument, and displays the body of the response

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "File '$2' not found!"
    exit 1
fi

# Check if the content of the file is valid JSON
if ! jq . "$2" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"

