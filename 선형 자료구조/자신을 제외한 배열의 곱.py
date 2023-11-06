# input : [1,2,3,4]
# output : [24,12,8,6]
# 단, 나눗셈을 하지 않고 O(n) 으로 문제를 해결해야 한다.
from typing import List

def productExceptSelf(a:List)->List:
    n = len(a)
    res = []
    for i in range(n):
        l = i-1
        r = i+1
        l_res = 1
        r_res = 1
        while l>=0:
            l_res*=a[l]
            l-=1
        while r<n:
            r_res*=a[r]
            r+=1
        res.append(l_res*r_res)
    return res


if __name__ == "__main__":
    a = list(map(int,input().split()))
    print(productExceptSelf(a))