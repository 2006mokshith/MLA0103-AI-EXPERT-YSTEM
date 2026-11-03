def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)

n = int(input("Enter a number: "))

print("Sum =", natural_sum(n))
