# Python typecasting each every type example program
a = "100"
b = int(a)
print(b, type(b))  # Output: 100 <class 'int'>

c = 45.67
ids = int(c)
print(ids, type(ids))  # Output: 45 <class 'int'>
# Note: Converting a float to int truncates the decimal part (it rounds toward zero).

e = 50
f = float(e)
print(f, type(f))  # Output: 50.0 <class 'float'>

g = "3.14"
h = float(g)
print(h, type(h))  # Output: 3.14 <class 'float'>

k = 25
m = str(k)
print(m, type(m))  # Output: 25 <class 'str'>

n = [1, 2, 3]
p = str(n)
print(p, type(p))  # Output: [1, 2, 3] <class 'str'>
# Note: The output looks like a list, but it is now a literal string of text characters.

q = (4, 5, 6)
r = list(q)
print(r, type(r))  # Output: [4, 5, 6] <class 'list'>

s = "xyz"
t = list(s)
print(t, type(t))  # Output: ['x', 'y', 'z'] <class 'list'>
# Note: Converting a string to a list breaks the string down into individual character elements.

u = [7, 8, 9]
v = tuple(u)
print(v, type(v))  # Output: (7, 8, 9) <class 'tuple'>

w = [1, 1, 2, 3]
x = set(w)
print(x, type(x))  # Output: {1, 2, 3} <class 'set'>
# Note: Sets automatically remove duplicate elements, which is why the extra 1 is gone.

y = [("key1", "value1"), ("key2", "value2")]
z = dict(y)
print(z, type(z))  # Output: {'key1': 'value1', 'key2': 'value2'} <class 'dict'>
# Note: To build a dict, the input must contain pairs (like a list of two-element tuples).

aa = 1
bb = bool(aa)
print(bb, type(bb))  # Output: True <class 'bool'>

cc = 0
dd = bool(cc)
print(dd, type(dd))  # Output: False <class 'bool'>
# Note: The integer 0 is evaluated as mathematically False in Python.

ee = ""
ff = bool(ee)
print(ff, type(ff))  # Output: False <class 'bool'>
# Note: Any empty sequence or collection (like an empty string "") evaluates to False.

gg = 7
hh = complex(gg)
print(hh, type(hh))  # Output: (7+0j) <class 'complex'>
# Note: This creates a complex number where 7 is the real part and 0j is the imaginary part.

ii=9
jj=complex(ii,7)
print(jj,type(jj)) # Output: (9+7j) <class 'complex>
# Note: In the conversion one type to complex type the default value of complex imaginary is 0j instead to change that we can also give number to imaginary part
