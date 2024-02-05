import collections

nums = [2,2,1,1,3]

count = collections.Counter(nums)

for c in count:
    print(count[c] , c)
    print()
    
