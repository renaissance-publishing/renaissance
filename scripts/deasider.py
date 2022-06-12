import re
import sys

#open_matcher = re.compile(r'<aside\s+class\s*=\s*"\s*(\w+)+"\s*>')
open_matcher = re.compile(r'<aside\s+class\s*=\s*"\s*(\w+\s*)+"\s*>')
#open_matcher = re.compile(r'<aside(.*)')
close_matcher = re.compile(r"</aside>")

def process(istream, ostream):
    in_asside = False
    line_num = 0
    for line in istream.readlines():
        line_num += 1

        if (lm := open_matcher.search(line)) is not None:
            if in_asside == True:
                raise Exception(f"Saw new asside block when already in an asside on line {line_num}")

            tag_type = lm.group(1).split()[0]
            #ostream.write(f"[[{lm.group(1)}]]\n")
            ostream.write(f"[[{tag_type}]]\n")
            in_asside = True

        elif (lm := close_matcher.search(line)) is not None:
            if in_asside == False:
                raise Exception(f"Encountered closing asside tag while not in an asside on line {line_num}")
            
            ostream.write("\n")
            in_asside = False

        else:
            if in_asside == True:
                ostream.write("|")
            ostream.write(line)

process(sys.stdin, sys.stdout)