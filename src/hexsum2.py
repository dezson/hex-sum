from __future__ import absolute_import
from __future__ import with_statement

import sys
from io import open

if len(sys.argv) != 2:
    print u"Syntax: {} <file>".format(__file__)
    sys.exit(2)

file = sys.argv[1]
hex_list = []
with open(file, u'rb') as fp:
     hex_list += [ord(c) for c in fp.read()]
print hex(sum(hex_list))
