import os
#ex 1
def list_directories_and_files(path):
    print("Directories:")
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            print(i)
    print("\nFiles:")
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            print(i)
path = input("Enter the path: ")
list_directories_and_files(path)

#ex 2
os.chdir('Lab_6')
pathe = input("Enter the path: ")
check = os.path.exists(pathe)
print(check)
file = open(pathe, 'r+')
print(file.read())
file.write(' this is added text')
file.close()
file = open(pathe, 'r')
print(file.read())
file.close()
print('\n')
file = open(pathe, 'r')
for i in file:
    print(i)
file.close()

#ex 3
def test_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Path exists")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path does not exist")
path = input("Enter the path: ")
test_path(path)

#ex 4
pathe = input('Enter the path: ')
file = open(pathe, 'r')
string_counter = 0
for i in file:
    string_counter += 1
print(string_counter)

#ex 5
listt = [str(x) for x in input().split()]
pathe = input('Enter the path: ')
file = open(pathe, 'a')
file.write(str(listt))
file.close()
file = open(pathe, 'r')
print(file.read())
file.close()

#ex 6
os.chdir('Lab_6')
pathe = input('Enter the path: ')
for i in range(65, 91):
    ascii_symbol = chr(i)
    filename = f'{ascii_symbol}.txt'
    file = open(os.path.join(pathe, filename), 'x')
    file.write(str(i))
file.close()

#ex 7
dirname = input('Enter dir name: ')
os.chdir(dirname)
pathe = input('Enter the path to file from wich we shoud copu text: ')
file = open(pathe, 'r')
copied_text = file.read()
file.close()
file_name = input('Enter filename which must be filled with copien text: ')
file = open(file_name, 'a')
file.write(copied_text)

#ex 8
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File '{path}' has been deleted")
    else:
        print(f"File '{path}' does not exist")
file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)