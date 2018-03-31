def xor_hex(string_1,string_2):
    xored = int(string_1,16) ^int(string_2,16) #int(x,16) : decode hex to int
    return hex(xored) # hex() encode int to hex
