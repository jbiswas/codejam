import sys
import string

GOOGLERESE = string.maketrans("pjdekrwoumyslcxvnitahfgbzq",
                              "rusoitfkjlangempbdwyxcvhqz")

N = int(sys.stdin.readline())
for case in range(1,N+1):
    text = sys.stdin.readline().strip().translate(GOOGLERESE)
    print "Case #%d: %s" %(case, text)


 
