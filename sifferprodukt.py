def no_zero(number):
    return [int(x) for x in str(number) if x!='0']

number = input()
arr_number = no_zero(number)

while len(arr_number) > 1:
    result = 1
    for digit in arr_number:
        result *= digit
    arr_number = no_zero(result)

print(arr_number[0])