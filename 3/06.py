a = list(map(int, input("입력: ").rstrip().split(',')))
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max)