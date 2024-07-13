#!/usr/bin/env bash
# returns the size of the body in bytes

if [ -z "$1" ]; then
   exit 1
fi

URL=$1
SIZE=$(curl -s -w '%{size_download}\n' -o /dev/null "$URL")
echo "$SIZE"
