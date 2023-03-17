#!/usr/bin/python3
duzen="abcçdefgğhiıjklmnoöprsştuüvyzxwq.,"
best_score = None
best_duzen = duzen
data = open("text","r").read()

def get_type_score():
    """type text and get score"""
    ret = 0
    for c in data:
        ret += get_score(c)
    return ret

def get_score(harf):
    """get character score by coordinate"""
    ret = 0
    if harf not in duzen:
        return 0
    num = duzen.index(harf) % 12 + 1
    if num == 4 or num == 7:
        ret = 4
    elif num == 3 or num == 5 or num == 6 or num == 8:
        ret = 3
    elif num == 2 or num == 9:
        ret = 2
    elif num == 1 or num == 10:
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
    """random mutation"""
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
        print(str(best_score)+"\n"+best_duzen[0:12]+"\n"+best_duzen[12:24]+"\n"+best_duzen[24:]+"\n\n")
    else:
        duzen = best_duzen
