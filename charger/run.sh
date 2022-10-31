#!/bin/bash

#Check if software is downloaded
if [[ !(`which svn` && `which latexmk` && `which python3`) ]]; then
    echo "[ERROR] Please install the following software or the equivalent on your system"
    echo "1. python3"
    echo "2. latexmk"
    echo "3. svn"
    exit 1
fi

#Download the source codes
svn co https://github.com/goats-9/ee3900-assignments/trunk/charger

#Run python codes
echo "Running python codes"
