import sys

if len(sys.argv) != 2:
    print("Syntax: {} <file>".format(__file__))
    sys.exit(2)

file = sys.argv[1]
hex_list = []
with open(file, 'rb') as fp:
    hex_list += [c for c in fp.read()]
print(hex(sum(hex_list)))
