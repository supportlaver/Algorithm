def reorderLogFiles(logs):
    alpha_list = []
    num_list = []
    for log in logs:
        split_log = log.split()
        if split_log[1].isdigit():
            num_list.append(log)
        else:
            alpha_list.append(log)
    
    alpha_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return alpha_list + num_list
    

logs = []
for _ in range(5):
    logs.append(input())
print(reorderLogFiles(logs))


