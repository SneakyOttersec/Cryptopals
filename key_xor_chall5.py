def xor(key,to_cipher,encoding="utf-8"):
    """
    I think that we can do that with differents way:
        The easier would be to iterate on j / i and increment but not sure if really pythonic
        The other way is to adapt the key size to the text size, not sure if pythonic but i'll go this way

    N.B : The encoding is really important, should use all the time utf-8 nowaday
    :param key:
    :param to_cipher:
    :return:
    """
    adapted_key = ''
    for i in range(len(to_cipher)):
        adapted_key += key[i % len(key)]
    b_key = adapted_key.encode(encoding)
    b_string = to_cipher.encode(encoding)
    f_string = ''

    for a,b in zip(b_key,b_string):
        f_string += chr(a^b)
    return f_string.encode(encoding).hex()




if __name__ == "__main__":
    xored = xor("ICE","Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
    print(xored)
