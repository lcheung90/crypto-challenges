def fixedXor(s1, s2):
    s1_digits = b64Digits(s1)
    s2_digits = b64Digits(s2)
    s1_xor_s2 = [ x ^ y for x, y in zip(s1_digits, s2_digits) ]
    hexified = map(lambda x: hex(x)[2:] if x > 9 else x, s1_xor_s2)
    stringy = map(lambda x: str(x), hexified)
    return ''.join(stringy)


def b64Digits(s):
    return map(lambda x: int(x, 16), s)
