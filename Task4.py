# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
os.system('cls')

def compress(s): # сжатие данных
    cmp = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        cmp += str(count) + s[i]
        i += 1
    return cmp

def recov(arh): #восстановление данных
    exp = ''
    for i in range(0, len(arh), 2):
        exp += int(arh[i]) * arh[i+1]
    return exp

with open('intext.txt', 'r') as f:
    st = f.read()

print(st)
rle = compress(st)
print(rle)

exp = recov(rle)
print(exp)

with open('outtext.txt', 'w') as f:
    f.write(exp)
