# 파일 다루기 read
f = open(r"ppap.txt", 'r')
while True:
    f_line = f.readline()
    if not f_line: break
    print(f_line, end='')
f.close()