def dyslectionarize(dic):
    longest = len(max(dic, key=len))
    for word in sorted(dic, key=lambda w: w[::-1]):
        spaces = ' '*(longest - len(word)) if longest!=len(word) else ''
        print('{}{}'.format(spaces,word))
        
dic=[]
while True:
    try:
        word = input()
        if word:
            dic.append(word)
        else:
            dyslectionarize(dic)
            print()
            dic=[]
    except EOFError:
        dyslectionarize(dic)
        break