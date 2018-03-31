import decipher_s_xor_chall3

final = []
with open("chall4.txt") as file:
    for i in file:
        r = decipher_s_xor_chall3.decipher_single_xor(i.rstrip())
        for j in r :
            final.append(j)
file.close()

final.sort(key=lambda x: x[0], reverse=True)
for i in range(10):
    print(final[i])
