numbers = [int(input()) for _ in range(10)]
result = list(map(lambda x: x % 42, numbers))
print(len(list(set(result))))