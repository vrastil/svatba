#!/bin/bash

# delete old files
THUMB_FILES=$(ls thumb*.{jpg,jpeg,.png} 2>/dev/null)
LG_HTML=lg_thumb.html

echo "" > $LG_HTML
rm $THUMB_FILES

# write new files
FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
let "i=1"
for f in $FILES
do
  # info
  printf "Converting $i\r"
  # create thumbnail
  convert -thumbnail x150 $f thumb.$f

  full="img/galery/katka/$f"
  thumb="img/galery/katka/thumb.$f"

  # thumbnail with link to full
  echo "<a class=\"lg-img\" data-src=\"$full\" data-exthumbimage=\"$thumb\" href>" >> $LG_HTML
  echo "  <img class=\"item\" src=\"$thumb\">" >> $LG_HTML
  echo "</a>" >> $LG_HTML
  i=$((i+1))
done
printf "\n"
