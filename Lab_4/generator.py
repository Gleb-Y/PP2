#ex 1
def gen_square(x):
    for i in range(x):
        yield (i + 1)**2
x = int(input())
p = gen_square(x)
cnt = 0
while cnt != x:
    print(next(p))
    cnt = cnt + 1

#ex 2
def print_even(v):
    for i in range(v+1):
        if i % 2 == 0:
            yield i
v = int(input())
h = print_even(v)

li = []
counter = 2
while counter != v:
    li.append(next(h))
    counter = counter + 1
s = str(li)[1:-1]
print(s)

#ex 3
def div_by_4_3(inp):
    for i in range(inp):
        if (i+1) % 3 ==0 and (i+1) %4 == 0:
            yield ((i+1))
inp = int(input())
a = div_by_4_3(inp)
count = 0
try:
    while 1:
        print(next(a), end=' ')
        count += 1
except StopIteration:
    pass

#ex 4
def squares(first, second):
    for i in range(first, second + 1):
        yield i**2
first = int(input())
second = int(input())
e = squares(first, second)
try:
    while 1:
        print(next(e), end=' ')
except StopIteration:
    pass

#ex 5
def from_n_to_0(f):
    while f != 0:
        yield f
        f -= 1
f = int(input())
a = from_n_to_0(f)
try:
    while 1:
        print(next(a), end=' ')
except StopIteration:
    pass
