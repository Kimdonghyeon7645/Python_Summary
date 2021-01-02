x, y = map(int, input().rstrip().split())
mine_map = []
for i in range(x):
    mine_map.append(list(input()))

for i in range(x):
    for j in range(y):
        if mine_map[i][j] is not '*':
            around = 0
            if i > 0:
                around += (1 if mine_map[i-1][j] is '*' else 0)
                if j > 0:
                    around += (1 if mine_map[i-1][j - 1] is '*' else 0)
                if j < x-1:
                    around += (1 if mine_map[i-1][j + 1] is '*' else 0)
            if i < x-1:
                around += (1 if mine_map[i+1][j] is '*' else 0)
                if j > 0:
                    around += (1 if mine_map[i+1][j - 1] is '*' else 0)
                if j < x-1:
                    around += (1 if mine_map[i+1][j + 1] is '*' else 0)
            if j > 0:
                around += (1 if mine_map[i][j-1] is '*' else 0)
            if j < x-1:
                around += (1 if mine_map[i][j+1] is '*' else 0)
            mine_map[i][j] = around

for col in mine_map:
    for cell in col:
        print(cell, end='')
    print()

"""
1시간컷,,
나는 아직도 코딩보단 삽질을 더 잘한다.
"""