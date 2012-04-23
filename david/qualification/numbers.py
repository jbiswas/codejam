import sys

def signature(N):
    result = N
    s = str(N)
    s = s[-1] + s[0:-1]
    M = int(s)
    while (M != N):
        if M < result:
            result = M
        s = s[-1] + s[0:-1]
        M = int(s)
    return result

def pairs(A, B):
    signatures = [signature(x) for x in range(A, B+1)]
    result = 0
    for n in range(len(signatures)-1):
        for m in range(n+1, len(signatures)):
            if signatures[n] == signatures[m]:
                result = result + 1
    return result

def fast_pairs(A, B):
    signatures = [signature(x) for x in range(A, B+1)]
    counts = {}
    result = 0
    for sig in signatures:
        if sig in counts.keys():
            counts[sig] = counts[sig] + 1
        else:
            counts[sig] = 1
    for (k,v) in counts.iteritems():
        result = result + comb(v)
    return result

def comb(n):
    return n*(n-1)/2
        
def main():
    N = int(sys.stdin.readline())
    for case in range(1,N+1):
        [A,B] = [int(x) for x in sys.stdin.readline().split()]
        print "Case #%d: %d" % (case, fast_pairs(A,B))

if __name__=="__main__":
    main()
