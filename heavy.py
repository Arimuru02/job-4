#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import groupby
x = 'процессор' + 'информация'
new_x = ''
for el,g in groupby(sorted(x)):
    if len(list(g)) == 1:
        new_x += el + ' '
print(new_x) 
