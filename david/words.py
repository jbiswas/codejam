from sys import stdin

N = stdin.readline()

for case in range(int(N)):
    print "Case #%i:" % (case+1),
    words = stdin.readline().split()
    words.reverse()
    for w in words:
        print w,
    print

