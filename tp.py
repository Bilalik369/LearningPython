def compter_pairs(sequence):
  
    count = 0
    for x in sequence:
        if x % 2 == 0:  
            count += 1
    return count
nums = [2, 5, 8, 11, 14, 7]
nums1 = [2, 5, 8, 2, 4, 8]

print(compter_pairs(nums))
print(compter_pairs(nums1))