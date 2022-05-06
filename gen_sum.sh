#! /bin/bash

printf "# Summary\\n\\n"

for file in [0-9]*.md ; do
    #echo "${file}"
    #TITLE_LINE=`grep 'title:\(.*\)' "${file}"`
    # one file has windows line-endings, because of course it does.
    # and that results in a stray \r being embedded in the title.
    # (and thanks to this SO for the one-liner: https://stackoverflow.com/questions/51995852/regular-expression-to-replace-m-with-n-or-to-remove-m)
    TITLE_LINE=`sed -e 's/\r//' < ${file} | grep 'title:' -`
    if [ $? -ne 0 ] ; then
        echo "$file: processing error, couldn't find title line." 1>&2
        continue
    fi
    TITLE_STRING="${TITLE_LINE#title: }"
    TITLE_STRING="${TITLE_STRING#\"}"
    TITLE_STRING="${TITLE_STRING%\"}"
    #TITLE_STRING="${TITLE_STRING/^M//}"
    if [ "x${TITLE_STRING}" == "x" ] ; then
        echo "$file: title string was blank" 1>&2
        continue
    fi
    echo "- [${TITLE_STRING}](./${file})"
done

echo
