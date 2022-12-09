import os

os.system("pip install --upgrade pip")
os.system("pip list > list.txt")
Lines = open('list.txt', 'r').readlines()
Lines = [i.split()[0] for i in Lines][2:]
for i in Lines:
    os.system("pip install --upgrade " + i)
