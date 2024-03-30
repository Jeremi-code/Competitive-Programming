n = int(input())
sentence = input()
sentence = sentence.lower()
dict = {}
if n < 26 :
      print('NO')
else :
    for i in range(n) :
        if sentence[i] in dict :
                dict[sentence[i]] += 1
        else :
                dict[sentence[i]] = 1
    dict_keys = list(dict.keys())
    if len(dict_keys) >=26 :
        print('YES')
    else :
        print('NO')