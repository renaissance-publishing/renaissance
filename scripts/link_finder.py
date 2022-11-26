#! /bin/python

import re
import sys
import os
import glob
import argparse

parser = argparse.ArgumentParser(prog = 'link_finder',
                                 description = 'A quick program to print links in md files')

parser.add_argument("--only-matches", "-m",
                    action="store_true",
                    help="Don't print the file name and number, just print the url.")
parser.add_argument("--only-broken", "-b",
                    action="store_true",
                    help="Only print broken links (supercedes --only-matches).")

args = parser.parse_args()

link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)") # now there's a fun one.

def line_iterator(file):
    """this exists because I need a function that'll return an iterator, to use with the enumerate function.
    (unfortunately, file.readlines returns a list).
    """

    for line in file:
        yield line

def enumerate_lines(file, starting_number=1):
    """I like to throw iterators at things.
    """

    line_num = starting_number
    for line in file:
        yield (line_num, line)
        line_num += 1

for file_name in glob.glob("*.md"):
    try:
        with open(file_name) as ifile:
            #for line_number, line in enumerate(ifile.readlines(), 1):
            for line_number, line in enumerate_lines(ifile):
                link_matches = link_re.findall(line)
                if link_matches is not None and len(link_matches) > 0:
                    for match in link_matches:
                        if args.only_broken:
                            if not os.path.exists(file_name):
                                sys.stdout.write(f"{match}\n")
                        elif args.only_matches:
                            sys.stdout.write(f"{match}\n")
                        else:
                            sys.stdout.write(f"{file_name} {line_number}: {match}\n")
    except Exception as e:
        sys.stderr.write(f"Encountered error while processing file {file_name}: {e}\n")
