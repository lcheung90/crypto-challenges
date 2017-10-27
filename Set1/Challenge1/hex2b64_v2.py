import codecs
import base64

def hex2b64(s):
    text = codecs.decode(s,'hex')
    return base64.b64encode(text)
