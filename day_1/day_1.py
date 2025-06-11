
#Print numbers from 1 to 100.

for i in range(1,101):
    print(i,end=" ")

#Print even numbers between 1 and 50.

for i in range(1,51):
    if i %2 == 0:
        print(i,end=" ")


#Calculate the factorial of a number using a loop.

n = int(input("Enter a number: "))
prod = 1
for i in range(n,1,-1):
    prod *= i
print(prod)


#Print the multiplication table of a number (e.g., 5).

n  = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{i} x {n} = {i*n}",end="\n")


#Sum of digits of a number (e.g., 1234 → 10).

n = int(input("Enter a number: "))
temp = n
sum = 0
while temp!=0 :
    v = temp% 10
    sum += v
    temp = temp //10
print(sum)





#Check if a number is a prime.

n = int(input("Enter a number: "))
if(n>0):
    flag = True
    for i in range(2,n):
        if(n%i == 0):
            flag = False
            
    if flag:
        print("prime")
    else:
        print("Not prime")


#Print the Fibonacci series up to n terms.

n = int(input("Enter the number limit: "))
a = -1
b = 1
for i in range(n):
    c = a+b
    a = b
    b = c
    print(c,end=" ")


#Count the number of vowels in a given string.

n = input("Enter a string: ")
l  = list(n)
print(l)
c= 0

for i in l:
    if i.upper() in ("A","E","I","O","U"):
        c+= 1
print(c)        


#Find the largest element in a list without using max().

l = [23,65,9,2,1,0,26]
max = 0
for i in l:
    if i>max:
        max = i
print(max)


#Count the frequency of each character in a string using a dictionary.

n = "Hello"
l = list(n)
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)



#Find all unique elements in a list.

l = [2,99,6,5,7,8,4,1,3,2,5,0,1,5,8,7,4]
l = set(l)
print(l)


#Merge two dictionaries.

d1 = {1:"a",2:"b",3:"c"}
d2 = {4:"d",5:"e",6:"f"}

d1.update(d2)
print(d1)

#Sort a list of tuples based on the second element.

l = ((4,3),(9,6),(3,2))

s = tuple(sorted(l,key = lambda x :x[1])) 
print(s)      

#Remove duplicates from a list.

l = [2,6,5,4,1,4,5,3,2,0,1,2,1,54,7,8,9,6]
l = set(l)
l = list(l)
print(l)
