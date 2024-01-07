# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:23:33 2024

@author: mmr78
"""

import random
import string

capitals = list( string.ascii_uppercase)
lowers = list (string.ascii_lowercase)
digits = list (string.digits)
signs = ['!', '$','&']
capital_letters = random.randint (2,4)
lower_letters = random.randint (2,4)
digit_numbers = random.randint(2, 3)
sign_number = random.randint (2,3)

total = []

for i in range(capital_letters):
    total.append(random.choice(capitals))
for i in range (lower_letters):
    total.append (random.choice(lowers))
for i in range (digit_numbers):
    total.append (random.choice(digits))
for i in range (sign_number):
    total.append (random.choice(signs))
random.shuffle(total)
password = ''
password = ''.join(total)
print (password)

