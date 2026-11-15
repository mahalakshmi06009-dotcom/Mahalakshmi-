def second_largest(nums):
    largest=second=None
    for n in nums:
        if largest is None or n>largest:
            second=largest
            largest=n
        elif n!=largest and (second is None or n>second):
            second=n
    return second

arr=[12,35,1,10,34,1]
print(second_largest(arr)) # 34
