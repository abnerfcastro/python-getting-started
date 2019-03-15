# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    # executes if for loop did not meet break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

def get_args():
    pass # Remember to implement this






