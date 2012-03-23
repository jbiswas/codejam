from sys import stdin

def find_matching_items_indices(credit, prices):
    for i in range(len(prices)):
        if prices[i] >= credit:
            continue
        for j in range(i+1, len(prices)):
            if prices[i] + prices[j] == credit:
                return [i+1,j+1]


N = int(stdin.readline())

for case in range(N):
    credit = int(stdin.readline())
    stdin.readline()
    prices = [int(price) for price in stdin.readline().split()]
    [i,j] = find_matching_items_indices(credit, prices)
    print "Case #%i: %i %i" % (case+1, i, j)
