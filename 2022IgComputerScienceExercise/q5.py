def b_d(bin):
    lst = list(str(bin))
    lst.reverse()
    power = 0
    su = 0
    while power < len(lst):
        value = int(lst[power])
        su += value * 2 ** power
        power += 1
    return su
def d_b(den,l,):
    if den == 0:
        return l*'0'
    d = den
    st = []
    while d > 0:
        re = d % 2
        st.append(str(re))
        d = d // 2
    #Add bit
    ct = len(st)
    while ct<l:
        st.append('0')
        ct+=1
    #reverse
    st.reverse()
    return st
def b_counter(bin,para=4,string = False):
    l = len(str(bin))
    d = b_d(bin)
    record = []
    for i in range(0,d+1):
        m = d_b(i, l)
        c = m.count('1')
        if c == para:
            record.append(m)
    return record
def main(a,k):
    lth = len(a)
    interpret = b_counter(lth*'1')
    counter = 0
    for i in interpret:
        result = []
        ct = 0
        base = 1
        while ct<lth:
            b =i[ct]
            if b=='1':
                base*=a[ct]
            ct+=1
        if base<=k:
            counter+=1
    return counter
print(main([1,1,4,5,1,4],7))
