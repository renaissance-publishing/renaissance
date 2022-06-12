#! /bin/bash

printf "# Summary\\n\\n"

for file in `for file in chapters/[0-9]*.md ; do echo "$file" ; done | sort -h` ; do
    TITLE_LINE=`sed -e 's/\r//' < ${file} | grep '^#[ \t]\+' -m 1`
    if [ $? -ne 0 ] ; then
        echo "$file: processing error, couldn't find title line." 1>&2
        continue
    fi

    TITLE_STRING="${TITLE_LINE#\# }"
    TITLE_STRING="${TITLE_STRING#\"}"
    TITLE_STRING="${TITLE_STRING%\"}"

    if [ "x${TITLE_STRING}" == "x" ] ; then
        echo "$file: title string was blank" 1>&2
        continue
    fi

    echo "- [${TITLE_STRING}](./${file})"
done

echo
