# Find Armstrong Numbers in the given range.

start, end = input("enter start and end point:\n").split()
number = int(start)
while number != int(end):
    sum = 0
    d_number= number
    x = len(str(number))
    while d_number != 0:
        num = d_number % 10
        d_number = int(d_number / 10)
        sum = sum + (num ** x)
    if sum == number:
        print(str(number) + " is amstrong number")
    number = number + 1
