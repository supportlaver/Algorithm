import collections
words = list(map(str,input().split()))
res = []
my_dict = collections.defaultdict(list)

for word in words:
    my_dict["".join(sorted(word))].append(word)

print(list(my_dict.values()))




