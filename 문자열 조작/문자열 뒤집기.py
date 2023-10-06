# 처음 푼 풀이 방식
def my_reverse(a):
    n = len(a)
    for i in range(n//2):
        a[i] , a[n-i-1] = a[n-i-1] , a[i]

# 다른 방법 (투 포인터를 이용한 스왑)

def two_pointer_reverse(a):
    s = 0
    e = len(a)-1

    while s<e:
        a[s] , a[e] = a[e] , a[s]
        s+=1
        e-=1

def reverse_string(a):
    a.reverse()
    
    

strs = list(map(str,input().split()))
reverse_string(strs)
print(strs)
