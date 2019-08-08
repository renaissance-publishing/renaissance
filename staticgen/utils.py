import re
import sys

toAnchorRegex = re.compile(r'[^\w\d]')

def get_element_contents(element):
    """try to merge the plain text of all children.
    I'm sure there's already a method for this but the documentation for mistletoe is god-awful.
    """

    contents = []

    # add this element's content, if it has any
    try:
        contents.append(str(element.content))
    except AttributeError:
        pass

    # get content from this elements children, if it has any
    try:
        for child in element.children:
            contents += flatten_to_text(child)
    except AttributeError:
        pass

    # there *has to be* some function in this API so that I don't have to do this.

    return contents

def flatten_to_text(element):
    contents = get_element_contents(element)
    return " ".join(contents)

def remove_nonword_chars(text):
    return toAnchorRegex.sub('', text)

def get_content(element, throw=True):
    """gets the content attribute of the first child.
    supports returning an empty string instead, so we can suppress errors to force a build through.
    """

    try:
        return element.children[0].content
    except:
        if throw:
            raise
        else:
            return ""

def dump_attrs(obj):
    """trivial function to dump the fields on an object,
    for use with markdown-parsing libraries with pathetically inadequate documentation.
    """

    for attr in dir(obj):
        sys.stdout.write(f"{attr} :  {getattr(obj, attr)}\n")