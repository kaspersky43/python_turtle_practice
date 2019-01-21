# printing prices formatted to the right
# input: 1234;234;456;456;567;567;678
# semicolon only as the divider
# 134000 -> 134,000

prices = list(map(int,input().split(';')))
prices.sort(reverse=True)
for p in prices:
    print('{0:>9,}'.format(p))
