from sys import argv

def fiblist(num):
    l = [0, 1]
    for i in range(num - 1):
        if (i % 2 == 0): l[0] = sum(l)
        else: l[1] = sum(l)
    print(l[num % 2])

print(fiblist(int(argv[1])))