#! /bin/bash

shopt -s extglob

for file in *.md
do
    # An extglob equivalent to the classic (([0-9])+.?)+
    #               v------------------- maximum match, rather than minimum
    #                 v----------------- extended glob, one-or-more repititions
    #                           V------- I think we have to do this because extglob is on?
    #                                    anyway, .? didn't work, at least for me.
    #                                V-- snip off the - that separates the chnum from the chname too
    new_name="${file##+(+([0-9])?(.))-}"

    echo "moving ${file} to ${new_name}"
    git mv "${file}" "${new_name}"
done

