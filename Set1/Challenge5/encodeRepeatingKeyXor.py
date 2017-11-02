def encodeRepeatingKeyXor(s, key):
    keySize = len(s)
    mask = expandToLength(key,keySize)
    xor = [ ord(x) ^ ord(y) for x, y in zip(s, mask) ]
    b16_xor_tokens = map(lambda x: hex(x), xor)
    return ''.join(map(lambda x: x[2:].zfill(2), b16_xor_tokens))

def expandToLength(s, length):
    return (s * ((length / len(s)) + 1))[:length]