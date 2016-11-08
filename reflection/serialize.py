import inspect
import re

################################################
###   Serialization to JSON

TAB = '\t'


def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''

    # Start with '{' for new object
    print("{")
    obj_fields = obj.__dict__

    # Add level for tabbing
    level += 1
    len_fields = len(obj_fields)

    for index, (k, v) in enumerate(obj_fields.items()):
        if '__dict__' in dir(v):
            # print line as TAB "k": "v", recurse on objects
            print("{}\"{}\": ".format(print_tabs(level), k), end='')
            to_json(v, level)
        else:
            # print comma except on last item
            last_comma = "" if index == len_fields - 1 else ","
            # print "v" when string
            if type(v) is str:
                v = escape_string(v)
                print("{}\"{}\": \"{}\"{}".format(print_tabs(level), k, v, last_comma))
            elif type(v) is bool or v is None:
                # Converting to null, true and false
                v = convert_bool(v)
                print("{}\"{}\": {}{}".format(print_tabs(level), k, v, last_comma))
            else:
                print("{}\"{}\": {}{}".format(print_tabs(level), k, v, last_comma))

        # if index == len_fields - 1:
        #     print('LAST', obj.__class__.__dict__)

    end_comma = "" if level == 1 else ","
    print("{}{}{}".format(print_tabs(level-1), '}', end_comma))


def print_tabs(level):
    tabs = ""
    for i in range(level):
        tabs+=str(TAB)
    return tabs

def convert_bool(v):
    if v is None:
        return 'null'
    else:
        return 'true' if v else 'false'

def escape_string(s):
    # escape " and /
    return re.sub(r"([\"\\])", r'\\\1', s)
