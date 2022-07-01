def mainplus(n):
    ct = 0
    while True:
        if n%2==0:
            n/=2
        else:
            n+=1
        if n==1:
            break
        ct+=1
    return ct

def mainminus(n):
    ct = 0
    while True:
        if n%2==0:
            n/=2
        else:
            n-=1
        if n==1:
            break
        ct+=1
    return ct

def main(number):
    a = mainplus(number)
    b = mainminus(number)
    return min(a,b)
number = 8

print(main(number))
