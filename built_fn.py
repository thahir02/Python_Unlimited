# some built-in function using with and without using bulit-in function
lst=['https.www.python','https.www.java','http.www.c','https.www.c++']

# concatenation without using bulit-in function
str1=""
for i in lst:
    str1 += i
print(str1)

# concationation using buit-in function join()
# built-in method is best ,memory efficient ,faster than the concateonation
str2="".join(lst)
print(str2)

# checking startswith the required characters without using built-in function
str3=""
for i in lst:
    if i[0:5:] == 'https':
        str3 += i
print(str3)

# checking startswith the required characters using built-in function startswith()
# if we want to give multiple values to startswith we sholud pass it as tuple
str4=""
for i in lst:
    if i.startswith("https"):
        str4 += i
print(str4)

# checking endswith the required characters without using built-in function
str5=""
for i in lst:
    if i[len(i)-3::] == 'c++' or i[len(i)-6::] == 'python':
        str5 += i
print(str5)

# checking endswith the required characters using built-in function
# if we want to give multiple values to endswith we sholud pass it as tuple
str6=""
for i in lst:
    if i.endswith(('python','c++')):
        str6 += i
print(str6)

# checking swapcase without using built-in function
str7=""
for i in lst:
    if i.islower():
        str7 += i.upper()
    else:
        str7 += i.lower()
print(str7)

# checking swapcase using built-in function
str8=""
for i in lst:
    str8 += i.swapcase()
print(str8)

# using built-in function in title(),capitalize
print("python programming is a high-level".title())
print("python programming is a high-level".capitalize())
