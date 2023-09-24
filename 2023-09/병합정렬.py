def Dsort(lt,rt):
    if lt<rt:
        mid = (lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)
        # 본연의 일
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid:
            tmp = tmp + arr[p1:mid+1]
        if p2<=rt:
            tmp = tmp + arr[p2:rt+1]

        # tmp  에 있는 것을 arr 에 복사
        # arr[i] = tmp[i] 이렇게 넣으면 안 됨
        # 그 이유는 (0,7) 에서 오른쪽 부분 4 5 6 7 인덱스에다가 tmp 값을 넣어야 하는데 
        # arr[i] = tmp[i] 로 하면 0 1 2 3 인덱스의 값으로 들어가기 때문이다.
        # 그래서 arr[lt+i] = tmp[i] 로 넣어줘야 제대로 된 인덱스로 들어간다.
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

if __name__=="__main__":
    arr = [23,11,45,36,15,67,33,21]
    print("Before sort : ",end=' ')
    print(arr)
    Dsort(0,7)
    print()
    print("After sort : ",end=" ")
    print(arr)
