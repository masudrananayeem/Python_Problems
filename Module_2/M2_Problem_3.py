list=[1,5,6,5,1,2,3]
duplicate = []

for num in list:
    if list.count(num) > 1 and item not in duplicate:
        duplicate.append(num)

print('Duplicate elements is : ', duplicate)
