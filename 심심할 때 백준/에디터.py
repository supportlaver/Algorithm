string = list(input())
n = int(input())
cursor = len(string)
for _ in range(n):
    print("cursor : ",cursor)
    print(string)
    temp = input().split()

    if temp[0] == "P":
        string.insert(cursor+1,temp[1])
    elif temp[0] == "L":
        if cursor == -1:
            continue
        else:
            cursor -= 1
    elif temp[0] == "D":
        if cursor == len(string):
            continue
        else:
            cursor += 1
    elif temp[0] == "B":
        if cursor == -1:
            continue
        else:
            string.remove(string[cursor-1])
            cursor -= 1
    
print(string)  