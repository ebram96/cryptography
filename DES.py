PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40,51, 45, 33, 48,
       44, 49, 39, 56,34, 53,
       46, 42, 50, 36, 29, 32]

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]


P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]


IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57, 25]


def printkey(lhs, key, sp):
    res = ""
    for i in range(0, len(key)):
        res += key[i]
        if (i + 1) % sp == 0:
            res += " "
    print(lhs + " = " + res)


def generate_from_table(key, table):
    new_key = ""
    for i in range(0, len(table)):
        new_key += key[table[i] - 1]
    return new_key


def generate_block_pairs(key):
    shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    C = key[:int(len(key)/2)]
    D = key[int(len(key)/2):]
    key_list = []
    for i in range(0, 16):
        for j in range(0, shift[i]):
            C += C[0]
            C = C[1:len(C)]
            D += D[0]
            D = D[1:len(D)]
        print("C" + str(i+1) + " = " + C)
        print("D" + str(i+1) + " = " + D + "\n")
        key_list.append(C + D)
    return key_list


def generate_subkeys(key_list):
    for i in range(0, len(key_list)):
        key_list[i] = generate_from_table(key_list[i], PC2)
        print("K%.2d = %s" % (i+1, key_list[i]))


def XOR(x, y):
    res = ""
    for i in range(0, len(x)):
        if x[i] == y[i]:
            res += '0'
        else:
            res += '1'
    return res


def f(key, block):
    block_expanded = generate_from_table(block, E)
    # print("E bit %s" % block_expanded)
    xor_res = ""
    xor_res = XOR(key, block_expanded)
    printkey("XOR" , xor_res, 6)
    sbox_ind = 0
    row = 0
    col = 0
    ind = 0
    b = ""
    res = ""
    for i in range(0, len(xor_res)):
        b += xor_res[i]
        sbox_ind += (i and i % 6 == 0);
        if len(b) % 6 == 0:
            row = int(b[0] + b[len(b)-1], 2)
            col = int(b[1:len(b)-1], 2)
            sbox_res = bin(S[sbox_ind][row][col])[2:]
            res += "0"*(4-len(sbox_res)) + sbox_res
            b = ""
    printkey("f", res, 4)
    res = generate_from_table(res, P)
    return res


def encrypt(dat, key_list):
    L = dat[:int(len(dat)/2)]
    R = dat[int(len(dat)/2):]
    new_L = ""
    new_R = ""
    for i in range(0, 16):
        print("Round %d:" % (i + 1))
        new_L = R
        new_R = XOR(L, f(key_list[i], R))
        L = new_L
        R = new_R
        # print("\nL = %s\nR = %s" % (L, R))
        printkey("L", L, 4)
        printkey("R", R, 4)
    # printkey("p_1 = ", generate_from_table(R+L, IP_1), 8)
    return generate_from_table(R+L, IP_1)


def hex_to_bin(hex):
    res = ""
    for i in range(0, len(hex)):
        s = bin(int(hex[i], 16))[2:]
        res += "0"*(4-len(s)) + s
    return res


def bin_to_hex(bin):
    res = ""
    i = 0
    while i < len(bin):
        res += hex(int(bin[i:i+4], 2))[2:]
        # print(len(hex(int(bin[i:i+4], 2))[2:]))
        i += 4
    res = res.upper()
    return res


hex_key = input("Enter encryption key in Hex: ")
key = hex_to_bin(hex_key)
printkey("Binary key", key, 8)
print("Generating PC-1 permutation for the key...")
key = generate_from_table(key, PC1)
printkey("PC-1 permutation of the key", key, 8)

print("Generating block pairs..")
key_list = generate_block_pairs(key)

print("Generating subkeys..")
generate_subkeys(key_list)

hex_dat = input("Enter your message (in hex) to encrypt: ")
dat = hex_to_bin(hex_dat)
print("\n\nApplying initial permutation to the 64-bit message..")
dat = generate_from_table(dat, IP)
printkey("Initial permutation of data", dat, 8)

print("Encrypting data...")
cipher = encrypt(dat, key_list)
printkey("Cipher Data (Binary)", cipher, 8)
cipher = bin_to_hex(cipher)
print("Cipher Data(Hex) = %s" % cipher)

# k = 133457799BBCDFF1
# m = 0123456789ABCDEF
