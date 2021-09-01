import sys

print(sys.argv)
msg = sys.argv[1]
cnt = int(sys.argv[2])

for i in range(cnt):
    print(i,msg)

