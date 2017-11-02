import re
import string

def detectSBX():
    lines = open('4.txt','r')
    printable = set(string.printable)

    for line in lines:
        s = brute_force(line.rstrip())
        if set(s).issubset(printable):
            d.append(s)

def genString(s, m):
    ascii_mask = map(lambda x: m, s)
    ascii_s = list(s.decode('hex'))
    xor = [ ord(x) ^ ord(y) for x, y in zip(ascii_s, ascii_mask) ]
    return ''.join(map(lambda x: chr(x),xor))

def brute_force(a):
    strings = {}
    current_max = 0
    c = ''

    for i in xrange(32,255,1):
        if re.match(r'\w',chr(i)):
            strings[chr(i)] = count_frequent(genString(a, chr(i)))

    for i in strings:
        if strings[i] > current_max:
            current_max = strings[i]
            c = i

    return c + ": " + genString(a,c)

def count_frequent(s):
    return reduce(lambda u, v: u + v, map(s.lower().count, 'etaoin shrdlu'))