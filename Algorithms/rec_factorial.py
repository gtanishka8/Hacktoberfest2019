def rec_factorial(n):
    if n == 1:
        return n
    else:
        return rec_factorial(n)*rec_factorial(n-1)
