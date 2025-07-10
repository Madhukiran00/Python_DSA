
# maximum number of consecutive 1's in the array.

nums=[0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0]
m= 0
count = 0
for i in range(len(nums)):
    if nums[i] == 1:
            count += 1
            if count>max:
             max=count
    else:
        count = 0
print(max) # 6


        