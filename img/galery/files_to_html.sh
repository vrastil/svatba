#!/bin/bash

FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
HTML_FILE=img.html
echo "" > $HTML_FILE
i=0
for f in $FILES
do
  ID="img_$i"
  echo "							<img class=\"item\" style=\"height:100%;max-height:250px;\" src=\"img/galery/$f\" alt=\"\">" >> $HTML_FILE
  i=i+1
done
