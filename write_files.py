import os

def cf(p, c):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, chr(119), encoding=chr(117)+chr(116)+chr(102)+chr(45)+chr(56)) as fh:
        fh.write(c)
    print(chr(67)+chr(114)+chr(101)+chr(97)+chr(116)+chr(101)+chr(100)+chr(58)+chr(32)+p)
print(chr(114)+chr(101)+chr(97)+chr(100)+chr(121))
