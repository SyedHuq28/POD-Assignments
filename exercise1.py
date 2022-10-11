import csv     # imports the csv module
import sys      # imports the sys module
from collections import defaultdict

def remove_space(sp):
    while("" in sp):
        sp.remove("")

def cal_average(num):
    sum_num = 0
    for t in num:
        
        x = float(t)
        sum_num = sum_num + x       

    avg = sum_num / len(num)
    return avg

def position(ps, y):
    for i in range(len(columns[5])):
        if(columns[5][i] == y):
            ps.append(i)
    l = []        
    for x in range(len(ps)):
        l.append(columns[7][ps[x]]) 
    return l

columns = defaultdict(list)
f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
reader = csv.reader(f)
lines= len(list(reader))
print (lines)

with open('TB_burden_countries_2014-09-29.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
new = columns[7].copy()


remove_space(new)    

print("The average value of e_prev_100k is", cal_average(new))

list2 = []
new2 = position(list2, "1990")
remove_space(new2)

print("The average value of e_prev_100k in 1990 is", cal_average(new2))

list3 = []
new3 = position(list2, "2011")
remove_space(new3)

print("The average value of e_prev_100k in 2011 is", cal_average(new3))
