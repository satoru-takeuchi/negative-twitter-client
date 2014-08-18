#!/bin/bash

if [ $# -lt 1 ] ; then
    echo "usage: $0 <target directory>" >&2
    exit 1
fi

TARGET_DIR="$1"

if [ ! -d "$TARGET_DIR" ] ; then
    echo "$0: '$TARGET_DIR' is not a valid directory"
    exit 1
fi

cp *.rb *.cgi *.html $TARGET_DIR
