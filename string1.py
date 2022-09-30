s = 'hi'
print(s)
print(s[1])
print(len(s))
print(s + ' there')
pi = 3.14
text = 'The value of pi is '  + str(pi)
print(text)
raw = 'india is my country'
print(raw)
multi = """It was the best of times.
It was the worst of times.
It was the beauty of times."""
print(multi)
str = "PYTHON TRAINING"
str.lower()
print(str.lower())
str1= " python training with google python class "
print(str1.upper())
print(str1.strip())
#print(str1.isalpha()) #check all the string characters classes
print(str1.startswith(' python')) #check weather the string strts with some string
print(str1.endswith(' ')) #check weather the string ends with some string
print(str1.find('google')) #to search a string and find the starting  index value
print(str1.find('arun')) # -1 for not found
print(str1.replace('class', 'course')) #replace an old string with new one
print(str1.split('a')) # to split a string to substring with given delimiter
str2 = "arun"
print("$".join(str2)) # join to a string
str3 = ["a", "r", "u", "n"]
print("".join(str3)) #joining with empty sring
str4 = 'hello'
print(str4[1:3]) # slices the string with index value
print(str4[1:]) #slices from index value 1
print(str4[:]) #no slices print full string
print(str4[1:100]) #index too high, truncated to string size
value = 2.791514
print(f'approximate value = {value:.2f}')  #  format the string to---approximate value = 2.79
car = {'tires': 4, 'doors': 2}
print(f'car = {car}')  # format the string car to----car = {'tires': 4, 'doors': 2}
# Split the line into chunks, which are concatenated automatically by Python
#adding values in to a tupple
str5 = ("%d dogs came, "
"They %s, and they %s, "
"and I'll %s them down."
% (5, 'bark', 'bite', 'knock')) # %d for int, %s for string, %f for float
print(str5)

