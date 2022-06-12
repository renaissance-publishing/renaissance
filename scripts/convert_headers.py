import re
import sys

in_header = False
found_header = False

delim_matcher = re.compile(r'^---+')

title_matcher = re.compile(r'title:(.*)')

for line in sys.stdin:
    if found_header == False and (lm := delim_matcher.match(line)) is not None:
        if in_header == False:
            in_header = True
        else:
            in_header = False
            found_header = True
    elif in_header == True and (lm := title_matcher.search(line)) is not None:
        title = str(lm.group(1)) # coerce to string, probably pointless
        title = title.strip()
        if title[0] == '"' and title[-1] == '"':
            title = title[1:-1]

        sys.stdout.write(f"# {title}\n")
    else:
        sys.stdout.write(line)

