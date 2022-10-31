#!/bin/bash

#Check if software is downloaded
if [[ !(`which svn` && `which ngspice` && `which latexmk` && `which python3`) ]]; then
    echo "[ERROR] Please install the following software or the equivalent on your system"
    echo "1. python3"
    echo "2. ngspice"
    echo "3. latexmk"
    echo "4. svn"
    exit 1
fi

#Download the source codes
echo "Downloading source codes..."
svn co https://github.com/goats-9/ee3900-assignments/trunk/charger
echo "DONE!"

#Run python codes
echo ""
echo "Running python codes..."
cd charger/codes
for file in *.py; do
    echo "Running python script $file"
    python3 $file > /dev/null 2>&1
done
echo "DONE!"

#Compile latex code
echo ""
echo "Compiling latex code..."
cd ..
latexmk -pdf main.tex > /dev/null 2>&1
echo "DONE!"

#View the pdf
echo ""
read -p "Would you like to see the PDF? [y/n] " see
if [[ $see == 'y' || $see == 'Y' || $see == '' ]]; then
    if [[ $TERMUX_VERSION ]]; then
        termux-open main.pdf
    else
        sh gopen.sh main.pdf
    fi
fi
