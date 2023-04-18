fact = lambda num: 1 if num == 0 else num * fact(num - 1)

series = lambda n, x: sum([(n ** i) / fact(i) for i in range(x + 1)])

n = float(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

result = series(n, x)

print("Result:", result)

result = 0


def calculate_sum(n):

    global result
    if n == 0:
        return

    calculate_sum(n - 1)
    result += ((-1) ** (n + 1)) / n



calculate_sum(n)


print("Result:", result)