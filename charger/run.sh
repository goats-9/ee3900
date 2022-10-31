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
echo "Downloading source codes"
svn co https://github.com/goats-9/ee3900-assignments/trunk/charger > /dev/null 2>&1
echo "DONE!"

#Run python codes
echo ""
echo "Running python codes"
cd charger/codes
for file in *.py; do
    echo $file
    python3 $file > /dev/null 2>&1
done
echo "DONE!"

#Compile latex code
echo ""
echo "Compiling latex code"
cd ..
latexmk -pdf main.tex > /dev/null 2>&1
echo "DONE!"

#(OPTIONAL) View the pdf
#termux-open main.pdf
#sh gopen.sh main.pdf
