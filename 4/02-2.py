y = dict(zip(range(1, 11), [2**i for i in range(1, 11)]))
for x in y:
    print(f"{x} - {y[x]}")
# y[x] = y.get(x)