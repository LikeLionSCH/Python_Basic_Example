import os

dir = input("Enter the foler name : ")
num = 15

try:
    if not(os.path.isdir(dir)):
        os.makedirs(os.path.join(dir))

except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

os.chdir(os.getcwd() + "/" + dir)

for i in range(1, num + 1):
    file = open(str(i) + ".py", "w")

file.close()
