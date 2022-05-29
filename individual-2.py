#!/usr/bin/env python3
# -*- coding: utf-8 -*-

line = list(input('Напечатайте предложение: ').split())
for ind in range(len(line) - 1):
    if line[ind] == line[ind + 1]:
        print(ind + 1, ind + 2)
        break
else:
    print('Таких нет!!!')
