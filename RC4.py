import numpy


def KSA(key):
    lst = list(range(0, 256))
    key_len = len(key)
    j = 0
    for i in range(0, 256):
        j = (j + lst[i] + key[i % key_len]) % 256
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def PRGA(key, iter):
    i = 0
    j = 0
    new_key = []
    while iter > 0:
        i = (i + 1) % 256
        j = (j + key[i]) % 256
        key[i], key[j] = key[j], key[i]
        new_key.append(key[(key[i] + key[j]) % 256])
        iter = iter-1
    return new_key


str_key = "3enab"
num_key = [ord(c) for c in str_key]

print("String key: \"" + str_key + "\"")
print("Respective numerical key array: ")
print(num_key)

msg = "This is my implementation for RC4 algorithm"
print("Message: \"" + msg + "\"")

permu = KSA(num_key)
key_stream = numpy.array(PRGA(permu, len(msg)))
# print("Key Stream: \"" + key_stream + "\"")
num_msg = numpy.array([ord(c) for c in msg])
print("Respective numerical message array: ")
print(num_msg)
cipher = num_msg ^ key_stream
cipher_hex = [hex(c) for c in cipher]
print("Cipher hex: ")
print(cipher_hex)
print("Cipher message: \"%s\"" % (''.join(chr(c) for c in cipher)))
