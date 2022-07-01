# 1 8 0     6 9
#6-9

def findStrobogrammatic(n):
    nums = n % 2 * list('018') or ['']
    while n > 1:
        n -=2
        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n < 2:] for num in nums]
        print(nums)
    return nums

findStrobogrammatic(4)
#print(findStrobogrammatic(4))