import os
path1 = "/home/asterisk/file.txt"
#file2 = open("/home/asterisk/file2.txt")



if os.path.isfile(path1):
    print("Файл существует. Вот он: \n")
    read_f = open(path1)
    print(read_f.read())
else:
    print("Файл не существует")

dir = os.path.abspath(os.curdir)
print(dir)

current_dir = os.getcwd()
print(current_dir)







