def blocks(n):
    if n <= 0:
        return 0
    else:
        return blocks(n - 1) + n


print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(8))
print(len(str(factorial(52))))


def print_count_down(n):
    if n <= 0:
        print("BOOM!")
        return
    print(n)
    print_count_down(n - 1)


print_count_down(5)
