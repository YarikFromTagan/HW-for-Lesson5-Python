# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls')

with open('text.txt', 'r', encoding="utf-8") as f:
    lst = f.read()
print(lst, '\n')

lst = lst.split(' ')
copy_lst = lst.copy()

for i in range(len(copy_lst)):
    if 'абв' in copy_lst[i]:
        del lst[i - len(copy_lst)]
                
lst = ' '.join(lst)
print(lst, '\n')