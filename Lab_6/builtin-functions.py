#ex 1
li1 = [int(x) for x in input().split()]
num = 1
for i in range(len(li1)):
    num *= li1[i]
print(num)

#ex 2
string = str(input())
cntr_A = 0
cntr_a = 0
for i in range(len(string)):
    if string[i].isupper():
        cntr_A += 1
    elif string[i].islower():
        cntr_a += 1
print('num of uppercase letters: ', cntr_A, ' num of lowercase letters: ', cntr_a, sep ='')

#ex 3
check = str(input())
check = list(check)
a = list(reversed(check))
if check == a:
    print(1)
else:
    print(0)

#ex 4
import time
import math
def root_after_miliseconds(num, mil):
    root = math.sqrt(num)
    time.sleep(mil / 1000)
    return root
number , milisec  = int(input()), int(input())
result = root_after_miliseconds(number, milisec)
print ('Square root of ', number, ' after ', milisec, 'miliseconds is ', result)    

#ex 5
tpl =tuple( int(x) for x in input().split() )
def pricol(num):
    if num:
        return True
    else:
        return False
lam = list(map(lambda element: pricol(element), tpl))
check = True
for i in range(len(lam)):
    if lam[i] == False:
        check = False
        break
    else:
        continue
print(check)
