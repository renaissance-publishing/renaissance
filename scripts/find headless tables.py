import sys
import re
import os

import argparse

custom_matcher = re.compile(r'\[\[([^| \t]+)[ \t]*(\|[ \t]*([^\]]*))?\]\]')

header_matcher = re.compile(r'\|[ \t]*-+[ \t]*\|')

def find_headerless(text_iter, name=None, verbose=False):
    in_custom = False

    in_table = False
    header_found = False
    table_start = None

    for line_num, line in enumerate(text_iter): # enumerate is lazy
        # boy howdy I sure do love hand-rolling state-machines

        # Need to keep the machinery to recognize custom-tags, since those lines also begin with |
        if (lm := custom_matcher.match(line)) is not None and in_custom == False:
            in_custom = True
        elif in_custom == True:
            if not line.startswith("|"):
                in_custom = False
        
        # now that we've excluded custom-tags, lines beginning with | are table-starts.
        # Or, well, could be, but let's not worry about that wrinkle right now.
        elif line.startswith("|"):
            if not in_table:
                in_table = True
                header_found = False
                table_start = (line_num, line)
                if verbose: sys.stdout.write(f"{name} {line_num} table start\n")
            #else:
            #    sys.stdout.write(f"{name} {line_num}\n")
            
            # let's test for a header-line even if we weren't in a table,
            # because I might have put a dash-row as a first-row somewhere.
            if header_found == False and (lm := header_matcher.search(line)) is not None:
                header_found = True
                if verbose: sys.stdout.write(f"{name} {line_num} header\n")
            elif verbose:
                if header_found:
                    sys.stdout.write(f"{name} {line_num} post-header\n")
                else:
                    sys.stdout.write(f"{name} {line_num} pre-header\n")

            # if the dash-row isn't the second row, that's not valid markdown, so we *should* alert on those.
            # but I don't care enough to handle that right now.
        # We were in a table, but this line didn't start with a pipe
        elif in_table == True:
            if verbose: sys.stdout.write(f"{name} {line_num} table ends\n\n")

            if header_found == False:
                if table_start is None:
                    raise Exception(f"internal error: tried to print table-found message, but table-start wasn't set")
                else:
                    if name is not None:
                        sys.stdout.write(f"{name} {table_start[0]}: {table_start[1]}\n")
                    else:
                        sys.stdout.write(f"{table_start[0]}: {table_start[1]}\n")

            in_table = False
            header_found = False
            table_start = None

    # Oh, right.  There won't be a non-table line after a table if the table ends the file.
    if in_table == True:
        if verbose: sys.stdout.write(f"{name} {line_num} table ends\n\n")

        if header_found == False:
            if table_start is None:
                raise Exception(f"internal error: tried to print table-found message, but table-start wasn't set")
            else:
                if name is not None:
                    sys.stdout.write(f"{name} {table_start[0]}: {table_start[1]}\n")
                else:
                    sys.stdout.write(f"{table_start[0]}: {table_start[1]}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fine \"malformed\" (i.e headerless) tables in markdown files")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='print out a message for every row of the table.')

    args = parser.parse_args()

    for root, dnames, fnames in os.walk("."):
        for fname in fnames:
            if not fname.endswith(".md"):
                continue

            try:
                with open(fname, "r") as ifile:
                    find_headerless(ifile, name=fname, verbose=args.verbose)
            except Exception as e:
                sys.stderr.write(f"Encountered processing error in {fname}: {e}\n")
