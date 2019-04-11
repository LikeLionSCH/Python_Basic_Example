import os

dir = input("Enter the foler name : ")
num = 15

os.chdir(os.getcwd() + "/" + dir)

for i in range(1, num + 1):
    file = open(str(i) + ".py", "w")

file.close()
