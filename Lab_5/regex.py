import re

# ex 1
protocol = re.compile('ab*')
st = str(input())
s = protocol.findall(st)
print(s)

# ex 2
prot = re.compile('ab{2,3}')
sti = str(input())
d = prot.findall(sti)
print(d)

# ex 3
pro = re.compile(r'[a-z]{1}_[a-z]{1}')
ti = str(input())
z = pro.findall(ti)
print(z)

# ex 4
pr = re.compile(r'[A-Z]{1}[a-z]+')
te = str(input())
v = pr.findall(te)
print(v)

# ex 5
pf = re.compile(r'a.+b')
to = str(input())
c = pf.findall(to)
print(c)

# ex 6
res = str(input())
def colon(textr):
    patrn = r'[ .,]'
    change = re.sub(patrn, ':', textr)
    return change
print(colon(res))

#ex 7
def snake_to_camel(snake_case):
    parts = snake_case.split('_')
    camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    return camel_case
snake_string = str(input())
camel_string = snake_to_camel(snake_string)
print(camel_string)  # Output: snakeCaseString

#ex 8
def split_at_uppercase(input_string):
    split_string = re.findall('[A-Z][^A-Z]*', input_string)
    return split_string
input_string = str(input())
split_string = split_at_uppercase(input_string)
print(split_string)  # Output: ['Split', 'This', 'String', 'At', 'Upper', 'Case', 'Letters']

#ex 9
def insert_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)
text = str(input())
formatted_text = insert_spaces(text)
print(formatted_text)  # Output: "This Is Camel Case String"

#ex 10
def camel_to_snake(camel_case):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_case = pattern.sub('_', camel_case).lower()
    return snake_case
camel_string = str(input())
snake_string = camel_to_snake(camel_string)
print(snake_string)  # Output: camel_case_string