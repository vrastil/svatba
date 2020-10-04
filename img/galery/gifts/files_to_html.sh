#!/bin/bash

# delete old files
THUMB_FILES=$(ls thumb*.{jpg,jpeg,.png} 2>/dev/null)
LG_HTML=lg_thumb.html

echo "" > $LG_HTML
rm $THUMB_FILES

# write new files
FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
i=0
for f in $FILES
do
  # create thumbnail
  convert -thumbnail x150 $f thumb.$f

  full="img/galery/gifts/$f"
  thumb="img/galery/gifts/thumb.$f"

  # thumbnail with link to full
  echo "<a class=\"lg-img\" data-src=\"$full\" data-exthumbimage=\"$thumb\" href>" >> $LG_HTML
  echo "  <img class=\"item\" src=\"$thumb\">" >> $LG_HTML
  echo "</a>" >> $LG_HTML
  i=i+1
done
