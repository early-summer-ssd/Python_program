import requests
import time
def format(number):
    gewei = str(number%10)
    shiwei = str(number//10%10)
    baiwei = str(number//100)
    result = baiwei + shiwei + gewei
    return result
page = 192
time_interval = 1
for i in range(1,page + 1):
    k = format(i)
    name = k + '.jpg'
    url = "https://resources.pearsonactivelearn.com/r00/r0087/r008797/r00879774/current/OPS/images/9781292244648-" +k+'.jpg'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}
    x = requests.get(url=url, headers=head)
    y = x.content
    with open(name, 'wb') as f:
        f.write(y)
    print('1',end='w')
    time.sleep(time_interval)
print("Finish")
