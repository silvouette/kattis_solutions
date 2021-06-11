total_person = int(input())
names = [str(input()) for _ in range(total_person)]

if names == sorted(names):
    print('INCREASING')
elif names == sorted(names,reverse=True):
    print('DECREASING')
else:
    print('NEITHER')