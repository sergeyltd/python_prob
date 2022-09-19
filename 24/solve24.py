import itertools
# from timeit import repeat

nums = [4,4,4,4]
all_results = set()
target = 7

def culc(a:int, b:int, operation:str) -> (int):
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b

    assert (False), "Not supported operation [{0}]".format(operation)

def find_solution4(nums, operations, target):
    try:
        sum = culc(culc(nums[0], nums[1], operations[0]), culc(nums[2], nums[3], operations[2]), operations[1])
        if sum == target:
            res = "({0}{1}{2}){3}({4}{5}{6})".format(nums[0],operations[0],nums[1],operations[1],nums[2],operations[2],nums[3],)
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    try:
        sum = culc(nums[0], culc(culc(nums[1], nums[2], operations[1]), nums[3], operations[2]), operations[0])
        if sum == target:
            res = "{0}{1}(({2}{3}{4}){5}{6})".format(nums[0],operations[0],nums[1],operations[1],nums[2],operations[2],nums[3],)
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    try:
        sum = culc(culc(nums[0], culc(nums[1], nums[2], operations[1]), operations[0]), nums[3], operations[2])
        if sum == target:
            res = "({0}{1}({2}{3}{4})){5}{6}".format(nums[0],operations[0],nums[1],operations[1],nums[2],operations[2],nums[3],)
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    try:
        sum = culc(culc(culc(nums[0], nums[1], operations[0]), nums[2], operations[1]), nums[3], operations[2])
        if sum == target:
            res = "(({0}{1}{2}){3}{4}){5}{6}".format(nums[0],operations[0],nums[1],operations[1],nums[2],operations[2],nums[3],)
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    try:
        sum = culc(nums[0],culc(nums[1], culc(nums[2], nums[3], operations[2]), operations[1]), operations[0])
        if sum == target:
            res = "{0}{1}({2}{3}({4}{5}{6}))".format(nums[0],operations[0],nums[1],operations[1],nums[2],operations[2],nums[3],)
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    return False

def find_solution3(nums, operations, target):
    try:
        sum = culc(culc(nums[0], nums[1], operations[0]), nums[2], operations[1])
        if sum == target:
            res = "({0}{1}{2}){3}{4}".format(nums[0],operations[0],nums[1],operations[1],nums[2])
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    try:
        sum = culc(nums[0], culc(nums[1], nums[2], operations[1]), operations[0])
        if sum == target:
            res = "{0}{1}({2}{3}{4})".format(nums[0],operations[0],nums[1],operations[1],nums[2])
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    return False

def find_solution2(nums, operations, target):
    try:
        sum = culc(nums[0], nums[1], operations[0])
        if sum == target:
            res = "{0}{1}{2}".format(nums[0],operations[0],nums[1])
            all_results.add(res)
            return True
    except ZeroDivisionError:
        pass

    return False

def find_all_solutions(nums, target):
    all_perms = list(itertools.permutations(nums, len(nums)))
    all_operations = list(itertools.product('+-*/', repeat=len(nums)-1))

    if len(nums) == 4:
        # break_2 = False
        for perms in all_perms:
            # if break_2: break
            for operations in all_operations:
                if find_solution4(perms, operations, target):
                    break_2 = True
    elif len(nums) == 3:
        # break_2 = False
        for perms in all_perms:
            # if break_2: break
            for operations in all_operations:
                if find_solution3(perms, operations, target):
                    break_2 = True
    elif len(nums) == 2:
        # break_2 = False
        for perms in all_perms:
            # if break_2: break
            for operations in all_operations:
                if find_solution2(perms, operations, target):
                    break_2 = True

find_all_solutions(nums, target)

all_nums3 = list()

num_length = len(nums)

for i in range(num_length):
    nums3 = nums[((i+1)//num_length):i] + nums[((i + 2)):] + [nums[i]*10 + nums[((i + 1)%num_length)]]
    all_nums3.append(nums3)

    nums3 = nums[((i+1)//num_length):i] + nums[((i + 2)):] + [nums[((i + 1)%num_length)]*10 + nums[i]]
    all_nums3.append(nums3)

for nums3 in all_nums3:
    find_all_solutions(nums3, target)

all_nums2 = [[nums[0]*10 + nums[1], nums[2]*10 + nums[3]],
             [nums[1]*10 + nums[0], nums[2]*10 + nums[3]],
             [nums[0]*10 + nums[1], nums[3]*10 + nums[2]],
             [nums[1]*10 + nums[0], nums[3]*10 + nums[2]],

             [nums[1]*10 + nums[2], nums[0]*10 + nums[3]],
             [nums[1]*10 + nums[2], nums[3]*10 + nums[0]],
             [nums[2]*10 + nums[1], nums[0]*10 + nums[3]],
             [nums[2]*10 + nums[1], nums[0]*10 + nums[3]],]

for nums2 in all_nums2:
    find_all_solutions(nums2, target)

all_unique_nums1 = set()

all_perm = list(itertools.permutations(nums, len(nums)))
for x in all_perm:
    all_unique_nums1.add(x[0]*1000 + x[1]*100 + x[2]*10 + x[3])

for x in all_unique_nums1:
    if x == target:
        all_results.add(x)


print("***********************************")
print("Input:                   {0}".format(nums))
print("Total found solutions:   {0}".format(len(all_results)))
print("All solutions:           {0}".format(all_results))






