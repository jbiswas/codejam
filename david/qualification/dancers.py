import sys

def canbesurprising(total):
    return total%3 != 1

def bestscore(total, surprise):
    if total%3 == 0:
        if surprise and total >= 2:
            return total/3 + 1
        else:
            return total/3
    elif total%3 == 1:
        return total/3 + 1
    else:
        if surprise:
            return total/3 + 2
        else:
            return total/3 + 1

def maxexceeding(p, totals, nsurprises):
    result = 0
    for total in totals:
        if not canbesurprising(total):
            if bestscore(total, False) >= p:
                result = result + 1
        else:
            if bestscore(total, False) >= p:
                result = result + 1
            else:
                if nsurprises > 0 and bestscore(total, True) >= p:
                    result = result + 1
                    nsurprises = nsurprises - 1
    return result

def main():
    N = int(sys.stdin.readline())
    for case in range(1, N+1):
        input = sys.stdin.readline().split()
        nsurprises = int(input[1])
        p = int(input[2])
        scores = [int(x) for x in input[3:]]
        print "Case #%d: %d" % (case, maxexceeding(p, scores, nsurprises))

if __name__ == "__main__":
    main()

    
                  
