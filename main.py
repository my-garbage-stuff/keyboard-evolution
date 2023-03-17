#!/usr/bin/python3
duzen="abcçdefgğhiıjklmnoöprsştuüvyzxwq.,"
best_score = None
best_duzen = duzen
data = open("text","r").read().lower()

cdata = {}

# train data set from text
for c in data:
    if c in cdata:
        cdata[c] += 1
    else:
        cdata[c] = 1

def get_type_score():
    """type text and get score"""
    ret = 0
    for c in duzen:
        if c in cdata:
            ret += cdata[c]*get_score(c)
    return ret

def get_score(harf):
    """get character score by coordinate"""
    ret = 0
    if harf not in duzen: # invalid character ignored
        return 0
    num = duzen.index(harf) % 12 
    if num == 3 or num == 6: # 1. finger
        ret = 4
    elif num == 2 or num == 6 or num == 5 or num == 7: # 2. finger or move 1. finger
        ret = 3
    elif num == 1 or num == 8: # 3. finger
        ret = 2
    elif num == 0 or num == 9: # 4. finger
        ret = 1
    else: # move 4. finger
        return 0

    row = int(duzen.index(harf) / 12)
    if row == 0 or row == 2: # top and bottom row
        return ret
    else:
        return ret + 1 # midle row

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
trynum = 0
while True:
    for i in range(1,int(len(duzen)/2)):
        mutation()
    trynum += 1
    score = get_type_score()
    if best_score < score:
        best_duzen = duzen
        best_score = score
        print("try: {}\nscore: {}\n  {}\n  {}\n  {}\n".format(
            str(trynum),
            str(best_score),
            best_duzen[0:12],
            best_duzen[12:24],
            best_duzen[24:]
        ))
    else:
        duzen = best_duzen
