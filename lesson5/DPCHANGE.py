__author__ = 'lenk'

MinNumCoins = {}
WCoins = {}

def DPCHANGE(money, coins):
    global MinNumCoins
    MinNumCoins[0] = 0
    WCoins[0] = []
    for m in range(1, money + 1):
        MinNumCoins[m] = -1
        for coin in coins:
            if m >= int(coin):
                if MinNumCoins[m - int(coin)] + 1 < MinNumCoins[m] or MinNumCoins[m] == -1:
                    MinNumCoins[m] = MinNumCoins[m - int(coin)] + 1
                    WCoins[m] = WCoins[m - int(coin)][:] + [coin]
        if len(MinNumCoins) > int(coins[0]):
            min = MinNumCoins.keys()
            min.sort()
            minK = min[0]
            del MinNumCoins[minK]
        print MinNumCoins

def main():
    global MinNumCoins
    global WCoins
    with open('inputDPC.txt', 'r') as fin:
        money = int(fin.readline())
        coins = fin.readline().split(',')

    DPCHANGE(money, coins)
    print(MinNumCoins[money])
    #print(WCoins[money])

main()