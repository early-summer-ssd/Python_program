def main(lst):
    result = []
    list_pos,list_neg = [],[]
    for i in lst:
        if int(i)>0:
            list_pos.append(i)
        elif int(i)<0:
            list_neg.append(i)
    while list_pos or list_neg:
        try:
            result.append(list_pos.pop())
            result.append(list_neg.pop())
        except IndexError:
            pass
    return result
a = [-1,-2,-3,4,5,6,9]
print(main(a))