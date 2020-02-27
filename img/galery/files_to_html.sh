#!/bin/bash

FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
HTML_FILE=img.html

for f in $FILES
do
  echo "							<img class=\"item\" src=\"img/galery/$f\" alt=\"\">" >> $HTML_FILE
done
