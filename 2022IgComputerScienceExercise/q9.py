def radixsort(inn):
    length = len(inn)
    if length == 1:
        return inn
    maximum = inn[0]
    for i in range(length):
        if inn[i]>maximum:
            maximum = inn[i]
    base = 0
    while 10**base<maximum:
        base+=1
    for currentbase in range(0,base):
        output = []
        bucket = [[],[],[],[],[],[],[],[],[],[]]
        for element in range(length):
            bucket[inn[element]//10**currentbase%10].append(inn[element])
        for sub_list in bucket:
            for element in sub_list:
                output.append(element)
        inn = output
    return output
def main(lst):
    lst = radixsort(lst)
    lst+=[0,0]
    result = []
    print(lst)
    ct = 0
    while ct<len(lst):
        if lst[ct]!=lst[ct+1]:
            tar = lst[ct+2]
            for i in lst[ct:ct+2]:
                if i!=tar:
                    result.append(i)
                    ct+=1
        else:
            ct+=2
    return result