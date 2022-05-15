import json
import sys
import re

# ripped from
#   https://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
# this should not have been necessary.

import codecs

ESCAPE_SEQUENCE_RE = re.compile(r'''
    ( \\U........      # 8-digit hex escapes
    | \\u....          # 4-digit hex escapes
    | \\x..            # 2-digit hex escapes
    | \\[0-7]{1,3}     # Octal escapes
    | \\N\{[^}]+\}     # Unicode characters by name
    | \\[\\'"abfnrtv]  # Single-character escapes
    )''', re.UNICODE | re.VERBOSE)

def decode_escapes(s):
    def decode_match(match):
        return codecs.decode(match.group(0), 'unicode-escape')

    return ESCAPE_SEQUENCE_RE.sub(decode_match, s)


# starting out with the default almost-no-op MD filter from
#   https://rust-lang.github.io/mdBook/for_developers/preprocessors.html

# custom_matcher = re.compile(r'\[\[([^|]+)|(.*)\]\]')
custom_matcher = re.compile(r'\[\[([^| \t]+)[ \t]*(\|[ \t]*([^\]]*))?\]\]')

def replace_customs(text):
    result = []
    in_custom = False

    #text = bytes(text, "UTF-8").decode("unicode_escape")
    #text = json.loads(text)
    text = decode_escapes(text)

    #with open("unescaped.md", "a") as ofile: ofile.write(">" + text + "\n")

    for line in text.split("\n"):
        if (lm := custom_matcher.match(line)) is not None and in_custom == False:
            in_custom = True
            result.append("<div class=\"asside\">")
            #result.append(f"groups: {lm.groups()}")
            if len(lm.groups()) >= 3 and (tm := lm.groups()[2]) is not None and len(tm)> 0:
                result.append(f"<div class=\"asside-title\">{tm}</div>")
        elif in_custom == True:
            if line.startswith("|"):
                result.append(line[1:])
            else:
                result.append("</div>")
                result.append(line)
                in_custom = False
        else:
            result.append(line)

    return "\n".join(result)

def process_chapter_rec(chapter):
    res = replace_customs( chapter['content'] )
    chapter['content'] = res

    if 'sub_items' in chapter:
        for sub_item in chapter['sub_items']: # chapter['sub_items'] is a list
            if 'Chapter' in sub_item: # each sub-item is a dict, which might have Chapter as a key
                process_chapter_rec(sub_item['Chapter'])

if __name__ == '__main__':
    if len(sys.argv) >= 2: # we check if we received any argument
        if sys.argv[1] == "supports" and sys.argv[2] == "html": 
            sys.exit(0)
        else:
            sys.exit(1)

    """
    ### Those escape sequences are in the text I get here
    inp = sys.stdin.read()
    with open("seen.json", "a") as ofile:
        ofile.write(inp)
    sys.stdout.write(inp)
    """

    """
    context, book = json.load(sys.stdin)
    
    with open("seen.json", "a") as ofile:
        ofile.write(json.dumps(book))
        ofile.write("\n")
        ofile.write(json.dumps(context))
        ofile.write("\n\n")

    print(json.dumps(book))
    """

    """
    context, book = json.load(sys.stdin)
    
    book['sections'][0]['Chapter']['content'] = "# what the fuck\n\nis going on?"

    with open("seen.json", "a") as ofile:
        ofile.write(json.dumps(book))
        ofile.write("\n")
        ofile.write(json.dumps(context))
        ofile.write("\n\n")

    print(json.dumps(book))
    """

    """
    context, book = json.load(sys.stdin)

    for section in book['sections']:
        in_custom = False
        for doc in section['Chapter']['content']: # idiot, that's `for doc in a str`
            res = replace_customs(doc)
            section['Chapter']['content'] = json.dumps(res)

    sys.stdout.write(json.dumps(book))
    """

    inp = sys.stdin.read()
    with open("inp.json", "a") as ofile: ofile.write(inp)
    context, book = json.loads(inp)

#    context, book = json.load(sys.stdin)

    for section in book['sections']:
        # the section headers show up as, well, sections.
        # that don't have Chapter elements.
        if 'Chapter' not in section:
            continue

        #res = replace_customs( section['Chapter']['content'] )
        #section['Chapter']['content'] = res
        process_chapter_rec(section['Chapter'])

    sys.stdout.write(json.dumps(book))