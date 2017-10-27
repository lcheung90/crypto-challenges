def hex2b64(s):
    digits = map(lambda t: int(t,16), s)
    bin_numbers = map(lambda x: bin(x)[2:].zfill(4), digits)
    bin_string = reduce(lambda u, v: u+v, bin_numbers)
    b64_bin_digits = [bin_string[i:i+6] for i in xrange(0,len(bin_string), 6)]
    b64 = map(lambda x: b64char(int(x,2)), b64_bin_digits)
    return ''.join(b64)

def b64char(i):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    return table[i]
