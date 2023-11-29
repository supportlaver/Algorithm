import sys
st1 = list(sys.stdin.readline().rstrip())
st2 = []
for _ in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()

    if temp[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif temp[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif temp[0] == "B":
        if st1:
            st1.pop()
    
    else:
        st1.append(temp[1])

st1.extend(reversed(st2))
print(''.join(st1))
