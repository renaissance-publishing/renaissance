#! /bin/python

"""
Some useful docs:
- Docstring conventions, because I'm a bad programmer: https://peps.python.org/pep-0257/
- The RE tutorial: https://docs.python.org/3/howto/regex.html
"""

import glob
import os, sys
import re

chs_matcher = re.compile(r"(([0-9]+\.?)+)(.*).md")

#subch_matcher = re.compile(r"[0-9]+\.[0-9]+(.*)\.md")
##subch_matcher = re.compile(r"[0-9]+\.[0-9]+")

sbreak_matcher = re.compile(r"[0-9]+(.*)\.sbreak")

title_matcher = re.compile(r"^\#+(.*)")

def extract_title(fname):
    """
    return the first thing that matches a markdown title element
    """

    with open(fname, "r") as ifile:
        for line in ifile:
            if (m := title_matcher.search(line)) is not None:
                title = m.group(1)
                if title is not None and len(title) > 0:
                    return title.strip()

    return None

def extract_section(fname):
    """
    return the first non-blank line.
    """
    
    with open(fname, "r") as ifile:
        while (line := ifile.readline()):
            line = line.strip()
            if len(line) > 0:
                return line
    
    return None


if __name__ == "__main__":

    ####
    # use a glob to grab the filenames

    fnames = glob.glob("chapters/[0-9]*")
    if fnames is None or len(fnames) < 1:
        sys.stderr.write("Could not find any chapters\n")
        sys.exit(1)
    
    fnames.sort()

    ####
    # iterate over the filenames

    for fname in fnames:
        # handle the section-break files
        if (m := sbreak_matcher.search(fname)) is not None:
            try:
                title = extract_section(fname)
                if title is not None and len(title) > 0:
                    sys.stdout.write(f"\n# {title}\n\n")
            except Exception as e:
                sys.stderr.write(f"Could not find section title for file: {fname}\n")
                continue

        # handle chapters and subchapters
        elif (m := chs_matcher.search(fname)) is not None:
            try:
                chapter_list = m.group(1) # it appears to be in order of opening parens,
                                          # except 0 is always the whole match
                subch_level = chapter_list.count(".")
                title = extract_title(fname)
                if title is None:
                    sys.stderr.write(f"Could not find title for file: {fname}\n")
                    continue
            except Exception as e:
                sys.stderr.write(f"Error while readinf file {fname}: {e}\n")
                continue

            sys.stdout.write(("  " * subch_level) + f"- [{title}]({fname})\n")
