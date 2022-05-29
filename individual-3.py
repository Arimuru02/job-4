#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def okiller(mstr):
    res = (''.join(char for n, char in enumerate(
        mstr) if not (char == 'о' and n % 2 == 0)))
    print(res)
if __name__ == '__main__':
    okiller(mstr='Самооборона, коловорот, колокол')
