colors = ["red","blue","green"]
print(colors[0])
print(colors[1])
print(len(colors))
#for----in
squares = [1,4,9,16,25]
sum = 0
for num in squares:
    sum += num
    print(sum)

# in list

names = ("arun","varun","govind")
if "arun" in names:
    print("yes")

#range
for i in range(25):
    print(i)

#while loop

## Access firdt element and every 3rd element in a list

a = [9,5,8,12,25,65,81,32,41,93]
i = 0
while i < len(a):
    print(a[i])
    i = i + 3

# to sort a list

list3 = [95,72,42,49,69,56]
list3.sort()
print (list3)

#list build up
list4 = []
list4.append("x")
list4.append("y")
print (list4)

#to slice a list

#list5 = ("x","y","z","o")
#print (list5[1:-1])
#list5 [0:2] = "p"
#print (list5)