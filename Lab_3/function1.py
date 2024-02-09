#ex 1
def ounces_to_grams(ounces):
    print(ounces*28.3495231 , 'grams')
ounces = int(input())
ounces_to_grams(ounces)

def grams_to_ounches(grams):
    print(grams/28.3495231 , 'ounches')
grams = int(input())
grams_to_ounches(grams)

#ex 2  
def to_centigrade(F):
    print('C = ' , (5 / 9) * (F - 32), sep="")
F = int(input())
to_centigrade(F)

#ex 3
def solve(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 4*r + 2*c == numlegs:
            return c, r
    return 'no solution'
numh = int(input())
numl = int(input())
print(solve(numh, numl))

#ex 4
def filter_prime(listmain):
    listb =[]
    for i in listmain:
        if i <= 2:
            continue
        t = True
        for k in range(2, i):
            if i % k == 0:
                t = False
                break
        if t:
            listb.append(i)
    for i in range(len(listb)):
        print(listb[i])

lista = []
b = 1
number = 1
while number != 0:
    number = int(input())
    if number != 0:
        lista.append(number)
    else:
        break
filter_prime(lista)

#ex 5
def gen_permutations(string, current_perm=''):
    if len(string) == 0:
        print(current_perm)
    else:
        for i in range(len(string)):
            new_string = string[:i] + string[i+1:]
            gen_permutations(new_string, current_perm + string[i])

str = input()
gen_permutations(str)

#ex 6
def rev(string):
    list_of_words = string.split()
    list_of_words.reverse()
    for i in list_of_words:
        print(i, end = ' ')

s = input()
rev(s)

#ex 7
def has_33(lis):
    for i in range(len(lis) - 2):
        if lis[i] == lis[i + 1] == 3:
            print('True')
            break
    else:
        print('False')
    pass
r = 1
lil = []

#ввод с клавиатуры:
while r != 0:
    r = int(input())
    if r != 0:
        lil.append(r)
has_33(lil)

#подготовленный ввод:
has_33([1,3,3,1])

#ex 8
def spy_game(array):
    for i in range(len(array) - 2):
        if array[i] == array[i + 1] == 0 and array[i + 2] == 7:
            return True
    return False
x = 1
input_list = [int(x) for x in input().split()]
print(spy_game(input_list))

#ex 9
def volume(r):
    vol = float((4*3.1415926535 * pow(r,3))/3)
    return vol
radius = float(input())
print(volume(radius))

#ex 10
def uniq(lis):
    lis2 = []
    for i in range(len(lis)):
        t = 1
        for j in range(len(lis2)):
            if lis[i] == lis2[j]:
                t = 0
                break
        if t == 1:
            lis2.append(lis[i])
    return lis2
inp_list = [int(x) for x in input().split()]
print(uniq(inp_list))

#ex 11
def palindrome(wrd):
    return wrd == wrd[::-1]
word = str(input())
print(palindrome(word))

#ex 12
def histogram(li):
    for i in li:
        print('*'*i)
in_list = [int(x) for x in input().split()]
histogram(in_list)

#ex 13
import random
print('Hello! What is your name?')
name = str(input())

print()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
guess_num = random.randint(1, 20)
print('Take a guess.')
number = int(input())
counter = 1
while number != guess_num:
    if number < guess_num:
        print()
        print('Your guess is too low.')
        number = int(input())
        counter += 1
    else:
        print()
        print('Your guess is too high.')
        number = int(input())
        counter += 1
else:
    print()
    print(f'Good job, {name}! You guessed my number in {counter} guesses!')