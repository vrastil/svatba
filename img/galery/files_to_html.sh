#!/bin/bash

# delete old files
THUMB_FILES=$(ls thumb*.{jpg,jpeg,.png} 2>/dev/null)
HTML_FILE=img.html
THUMB_HTML_FILE=thumb.html
LG_HTML=lg_thumb.html

echo "" > $HTML_FILE
echo "" > $THUMB_HTML_FILE
echo "" > $LG_HTML
rm $THUMB_FILES

# write new files
FILES=$(ls *.{jpg,jpeg,.png} 2>/dev/null)
i=0
for f in $FILES
do
  # create thumbnail
  convert -thumbnail x150 $f thumb.$f

  # full images
  echo "<img class=\"item\" src=\"img/galery/$f\">" >> $HTML_FILE

  # thumbnail only
  echo "<img class=\"item\" src=\"img/galery/thumb.$f\">" >> $THUMB_HTML_FILE

  # thumbnail with link to full
  echo "<a class=\"lg-img\" data-src=\"img/galery/$f\" href=\"img/galery/$f\">" >> $LG_HTML
  echo "  <img class=\"item\" src=\"img/galery/thumb.$f\">" >> $LG_HTML
  echo "</a>" >> $LG_HTML
  i=i+1
done
