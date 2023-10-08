import re , collections
# https://cosmosproject.tistory.com/180
paragraph = input()
banned = input()

words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

# 첫 번째 방법
counts = collections.defaultdict(int)
for word in words:
    counts[word]+=1

print(max(counts,key=counts.get))

# 두 번째 방법
se_counts = collections.Counter(words)
print(se_counts.most_common(1)[0][0])

    


