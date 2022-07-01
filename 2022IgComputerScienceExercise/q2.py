def power(num):
    if num%2==1:
        return False
    while num>=1:
        num/=2
        if num == 1:
            return True
    return False
print(power(-1))#
