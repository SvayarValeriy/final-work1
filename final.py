def isSmaller(x):
    return len(x)<=3


arr = ['123', 'NY', 'этоМассив', ':=))', 'LA', 'неСмешно', '15']
filteredList = list(filter(isSmaller, arr))

print(str(filteredList))