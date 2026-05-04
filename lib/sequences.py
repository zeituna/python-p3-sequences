def print_fibonacci(n):
    fib = []

    # Handle edge cases
    if n <= 0:
        print(fib)
        return

    if n >= 1:
        fib.append(0)
    if n >= 2:
        fib.append(1)

    # Generate remaining numbers
    for i in range(2, n):
        next_num = fib[i - 1] + fib[i - 2]
        fib.append(next_num)

    print(fib)