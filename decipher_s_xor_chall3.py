

# Occurence frenquency from wikipédia

list_letter_en = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.0095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
    ' ': 0.1918182
}
def decipher_single_xor(string_1):
    result_l = []
    hex_1 = bytearray.fromhex(string_1)
    for i in range(256):
        xored = ''
        for hex_s in hex_1:
            xored += chr(i ^ hex_s)
            score = occurence(xored)
        if score > 0 :
            result_l.append([score,xored])

    result_l.sort(key=lambda x: x[0], reverse=True) #Descending to go from the highest to the lowest
    return result_l


def occurence(xored_string):
    scoring = 0
    for i in xored_string:
        if i in list_letter_en:
            scoring += list_letter_en[i] # Add a score based on the occurence : a bit bullshit but work for basic words
    return scoring
