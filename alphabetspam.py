import sys
def get_ints(): return list(map(str, sys.stdin.readline().strip()))
spam = get_ints()
counter = [0, 0, 0, 0]

for character in spam:
    if character == '_':
        counter[0] += 1
    elif character.islower():
        counter[1] += 1
    elif character.isupper():
        counter[2] += 1
    else:
        counter[3] += 1

for result in counter:
    print("{:.16f}".format(result/len(spam)))
