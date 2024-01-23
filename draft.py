import time

sd = int(input())
if sd >= 2:
    print('lol')
elif sd == 1 and sd >0 or sd == -1:
    print('nah')
else:
    print('sheesh')

while sd <=0:
    print('nope')
    time.sleep(1)
    sd = sd + 1

print('lol' + 5) #error tak nelzya