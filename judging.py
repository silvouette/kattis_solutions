submission = int(input())
dom = sorted([input() for _ in range(submission)])
kat = sorted([input() for _ in range(submission)])

a = 0
b = 0
res = 0

while(a<submission and b<submission):
    if(dom[a] == kat[b]):
        a+=1
        b+=1
        res+=1
    elif(dom[a] < kat[b]):
        a+=1
    else:
        b+=1
print(res)
    
