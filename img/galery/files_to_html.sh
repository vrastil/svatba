#!/bin/bash

# delete old files
THUMB_FILES=$(ls thumb*.{jpg,jpeg,.png} 2>/dev/null)
HTML_FILE=img.html
THUMB_HTML_FILE=thumb.html

echo "" > $HTML_FILE
echo "" > $THUMB_HTML_FILE
rm $THUMB_FILES

# write new files
FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
i=0
for f in $FILES
do
  # create thumbnail
  convert -thumbnail x200 $f thumb.$f
  echo "<img class=\"item\" src=\"img/galery/$f\">" >> $HTML_FILE
  echo "<img class=\"item\" src=\"img/galery/thumb.$f\">" >> $THUMB_HTML_FILE
  i=i+1
done
