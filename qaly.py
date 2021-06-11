import sys
def get_qaly(): 
    q_y = list(map(float, sys.stdin.readline().strip().split()))
    return q_y[0]*q_y[1]

periods = int(input())
qaly = [get_qaly() for _ in range(periods)]
print('{:.3f}'.format(sum(qaly)))