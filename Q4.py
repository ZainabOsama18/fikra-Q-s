#combines 2 lists
#
x1=[1,2,3,4,5]
x2=["a","b","c","d","e"]

z=len(x1)

m=[ ]
for i in range (z):
   m.append(x1[i])
   m.append(x2[i])
   
print (m)

