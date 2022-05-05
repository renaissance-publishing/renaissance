#! /bin/python3

import sys
import os
import re
import argparse
import subprocess

parser = argparse.ArgumentParser(description="shift chapter numbers up or down.")
parser.add_argument('--start', '-s', default=0,
                    type=int,
                    help="Where to start")
parser.add_argument('--end', '-e', default=None,
                    type=int,
                    help="Where to stop (exclusive)")
parser.add_argument('--increment', '--incr', '-i', default=1,
                    type=int,
                    help="How much to shift each chapter number")
args = parser.parse_args()

if args.end is not None and args.end == args.start:
    sys.stderr.write(f"start and end must be different (both where {args.start}\n")
    sys.exit(1)

if args.end is not None and args.end < args.start:
    sys.stderr.write(f"start muus be greater than end (start was {args.start}, end was {args.end}\n")
    sys.exit(2)

ch_name_matcher = re.compile(r"^([0-9]+)(.*)")

for fname in os.listdir():
    match = ch_name_matcher.match(fname)
    if match is None:
        continue

    try:
        ch_num = int(match.group(1))
    except:
        sys.stderr.write(f"Encountered an error while parsing chapter number in {fname}\n")
        continue

    ch_title = str(match.group(2))

    if ch_num < args.start: continue
    if args.end is not None and ch_num >= args.end: continue

    #print(f"{fname} {ch_num}")
    #sys.stdout.write(f"fname: {fname}\nch_num: {ch_num}\nch_title: {ch_title}\n")
    new_fname = str(ch_num + args.increment) + ch_title
    try:
        subprocess.run(["git", "mv", fname, new_fname], capture_output=False)
    except e:
        sys.stderr.write(f"encountere error while trying to call `git miv`: {e}\n")
    #sys.stdout.write(" ".join(["git", "mv", fname, new_fname]) + "\n")
