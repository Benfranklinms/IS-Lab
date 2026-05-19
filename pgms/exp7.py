import os

src = input("enter source location : ")
des = input("enter destination location : ")

fd1 = os.open(src, os.O_RDONLY)
data = os.read(fd1, 1024)

fd2 = os.open(des, os.O_WRONLY)
os.write(fd2, data)

os.close(fd1)
os.close(fd2)

print("file copied")
