import sys
from typing import List

def maxProf_1(price:List[int])->int:
    n = len(price)
    maxx = -2147000000
    for i in range(n-1):
        x = price[i]
        for j in range(i+1,n):
            if x < price[j]:
                maxx = max(maxx,price[j]-x)
    return maxx

def maxProf_2(price:List[int])->int:
    n = len(price)
    maxx = -2147000000
    for i in range(n-1):
        maxx = max(maxx , max(price[i+1:])-price[i])
    return maxx

def maxProf_3(prices:List[int])->int:
    # 입력값 price 가 [] 로만 들어올 수 있기 떄문에 -sys.maxsize 가 아닌 0 으로 초기화
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price,price)
        profit = max(profit,price-min_price)
    
    return profit

        

# n^2 한 번 해보고
# 슬라이싱으로 한 번 해보고



if __name__ == "__main__":
    price = list(map(int,input().split()))
    print(maxProf_2(price))
