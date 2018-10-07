# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:22:58 2018

@author: Somesh
"""

summ = 0
digit_sum = 0
i = 0
while i < 1000000:
    j = list(str(i))
    for x in j:
       digit = int(x) ** 5
       digit_sum += digit
    if digit_sum == i:
       summ += i
       print(i)
    else:
       digit_sum = 0
    i += 1
    digit_sum = 0
print(summ)