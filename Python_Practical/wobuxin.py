
# # Fibonaaci sequence

def fibonacci(n):
    fibonacci_list = [0,1]
    for i in range(n-2):
        fibonacci_list.append(fibonacci_list[-2]+fibonacci_list[-1])
    return fibonacci_list
print(fibonacci(10))


# # Given nums = [2, 7, 11, 15], target = 9,
# # Because nums[0] + nums[1] = 2 + 7 = 9,
# # return [0, 1].
nums = [2, 7, 11, 15]
target = 9
def twoSum(nums, target):
    result = []
    for n in range(0, len(nums)):
        for j in range(n+1, len(nums)):
            if nums[j] == target-nums[n]:
                result.append(n)
                result.append(j)
    return result

# ## Use dict to increase the efficiency

def twoSum_better(nums,target):
    result = []
    dict = {}
    for i in range(0, len(nums)):
        dict[nums[i]] = i
    for n in range(0, len(nums)):
        mama = target - nums[n]
        if mama in dict and mama != n:
            result.append(dict[nums[n]])
            result.append(dict[mama])
            return result

print(twoSum(nums,target))


# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(x):
    if x >= 0:
        x = int(str(x)[::-1])
    else:
        x = int("-"+str(x)[::-1][:-1])
    if -2 ** 31 <= x <= 2 ** 31 - 1:
        return x
    else:
        return 0

print(reverse(-123))




