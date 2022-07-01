def sqrt(num):
    if num**0.5%1 == 0:
        print('True,sqrt(%d)=%d'%(num,num**0.5))
    else:
        print('False,sqrt(%d)=%.2f'%(num,num**0.5))
