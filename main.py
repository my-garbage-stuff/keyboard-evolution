#!/usr/bin/env python
duzen="abcçdefgğhiıjklmnoöprsştuüvyzxwq.,"
best_score = None
best_duzen = duzen
data = open("text","r").read()


def get_type_score():
    """type text and calculate score"""
    ret = 0
    for c in data:
        ret += get_score(c)
    return ret

def get_score(harf):
    """get character score by coorditane"""
    ret = 0
    if harf not in duzen:
        return 0
    num = duzen.index(harf) % 12 + 1
    if num == 5 or num == 4:
        ret = 4
    elif num == 3 or num == 6:
        ret = 3
    elif num == 2 or num == 7:
        ret = 2
    elif num == 1 or num == 8:
        ret = 1
    else:
        return 0
    row = int(duzen.index(harf) / 12)
    if row == 0 or row == 2:
        return ret + 0
    else:
        return ret + 1

import random

def mutation():
    """random mutation generator"""
    global duzen
    i = random.randint(0, len(duzen)-1)
    j = random.randint(0, len(duzen)-1)
    c = duzen[i]
    k = duzen[j]
    duzen = duzen.replace(c,"@")
    duzen = duzen.replace(k,c)
    duzen = duzen.replace("@",k)

best_score = get_type_score()
while True:
    mutation()
    score = get_type_score()
    if best_score > score:
        best_duzen = duzen
        best_score = score
        print(score, best_duzen)
    else:
        duzen = best_duzen
