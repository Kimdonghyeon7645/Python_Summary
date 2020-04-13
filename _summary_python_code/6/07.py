# 파일 다루기 write
f = open(r"ppap.txt", 'w')
for i in range(1, 5):
    f.write("집에 가고 싶다\n")
f.close()