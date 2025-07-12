list=[1,5,6,5,1,2,3]
duplicate = []

for item in list:
    if list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)

print('Duplicate elements is : ', duplicate)
