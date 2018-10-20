
import csv
from collections import Counter

array = []  
with open('oscar.csv','r') as file:
    reader = csv.reader(file)
    
    for line in reader:
            array.append(line[3])
            count = Counter(array) 
file.close()




counter = 0
actor_name = ""
for name , num in count.items():
    if counter < int(num):
        counter = num
        actor_name = name



print(actor_name)
    

older=3000
with open ('oscar.csv','r') as f:
    r=csv.reader(f)
    for i in r:
        if older > int(i[1]):
            older =int(i[1])
            w=older
            w2=i[4]
            r=i[3]

print(r+"has oldest oscar in year :" +str(w)+"in filem "+str(w2))          

f.close()