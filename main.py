from Crypto.Cipher.AES import AESCipher

import base64
import itertools

data = "" #TODO: request data
pass_list = itertools.combinations("1234567890", 4)

for key in pass_list:
    try:
        data = base64.b64decode(data)
        new_data = AESCipher("".join(key).decrypt(data)
        if new_data.find("IceCTF")!=-1:
            print "".join(key)."\n"
            print new_data
    except:
        continue