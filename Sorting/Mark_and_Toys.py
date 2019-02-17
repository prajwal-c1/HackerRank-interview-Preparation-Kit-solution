
# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    s=0
    for i in range(len(prices)):
        s+=prices[i]
        if(s>=k):
            print(i)
            break


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    

