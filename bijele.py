import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def add_remove(piece_found, piece_proper):
    if piece_found != piece_proper :
        return piece_proper - piece_found
    else:
        return 0

found = get_ints()
proper = [1, 1, 2, 2, 2, 8]

result = list(map(add_remove, found, proper))
print(" ".join(map(str,result)))