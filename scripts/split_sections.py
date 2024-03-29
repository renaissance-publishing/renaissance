import sys
import os
import re

heading_matcher = re.compile(r"^\#\#\s+(.*)")
chapnum_matcher = re.compile(r"^(\d+)")

for fname in sys.argv[1:]:
    try:
        with open(fname, "r") as ifile:
            section_no = 0
            section_name = None
            ofile = None

            basename = os.path.basename(fname)
            if basename is None or len(basename) < 1:
                raise Exception("Could not determine basename.")

            chapnum_m = chapnum_matcher.match(basename)

            #ofname = basename + "_" + section + ".md"
            #ofname = f"{basename}_{section_no}.md"
            #print(ofname)
            #ofile = open(ofname, "w")

            for line in ifile:
                m = heading_matcher.match(line)
                if m is not None:
                    section_no += 1
                    section_name = m.group(1)
                    sys.stdout.write(f"encountered start of section {section_no}: \"{section_name}\"\n")

                    if ofile is not None and not ofile.closed:
                        ofile.close()
                    #ofname = f"{basename}_{section_no}_{section_name}.md"
                    if chapnum_m is not None:
                        ofname = f"{chapnum_m.group(1)}.{section_no}-{section_name}.md"
                    else:
                        ofname = f"{basename}_{section_no}_{section_name}.md"
                    ofile = open(ofname, "w")
                elif ofile is not None and not ofile.closed:
                    ofile.write(line)

    except Exception as e:
        sys.stderr.write(f"Processing file \"{fname}\" failed with error: {e}.\n")
        
