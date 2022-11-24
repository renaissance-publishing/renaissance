#! /bin/python

import glob
import os, sys
import re

subch_matcher = re.compile(r"[0-9]+\.[0-9]+(.*)\.md")
#subch_matcher = re.compile(r"[0-9]+\.[0-9]+")

sbreak_matcher = re.compile(r"[0-9]+\~(.*)\.sbreak")

title_matcher = re.compile(r"^\#+(.*)")

def extract_title(fname):
    with open(fname, "r") as ifile:
        for line in ifile:
            if (m := title_matcher.search(line)) is not None:
                title = m.group(1)
                if title is not None and len(title) > 0:
                    return title.strip()

    return None

if __name__ == "__main__":

    fnames = glob.glob("chapters/[0-9]*")
    if fnames is None or len(fnames) < 1:
        sys.stderr.write("Could not find any chapters\n")
        sys.exit(1)
    
    fnames.sort()

    for fname in fnames:
        if (m := sbreak_matcher.search(fname)) is not None:
            title = m.group(1)
            if title is not None and len(title) > 0:
                sys.stdout.write(f"\n\# {title}\n\n")
        elif (m := subch_matcher.search(fname)) is not None:
            try:
                title = extract_title(fname)
                if title is None:
                    sys.stderr.write(f"Could not find title for file: {fname}\n")    
                    continue
            except Exception as e:
                sys.stderr.write(f"Error while reading file {fname}: {e}\n")
                continue

            sys.stdout.write(f"  - [{title}]({fname})\n")

        else:
            try:
                title = extract_title(fname)
                if title is None:
                    sys.stderr.write(f"Could not find title for file: {fname}\n")    
                    continue
            except Exception as e:
                sys.stderr.write(f"Error while reading file: {fname}: {e}\n")
                continue

            sys.stdout.write(f"- [{title}]({fname})\n")
