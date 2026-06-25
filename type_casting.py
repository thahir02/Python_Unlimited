# Python typecasting each every type example program
a = "100"
b = int(a)
print(b, type(b))

c = 45.67
ids = int(c)
print(ids, type(ids))

e = 50
f = float(e)
print(f, type(f))

g = "3.14"
h = float(g)
print(h, type(h))

k = 25
m = str(k)
print(m, type(m))

n = [1, 2, 3]
p = str(n)
print(p, type(p))

q = (4, 5, 6)
r = list(q)
print(r, type(r))

s = "xyz"
t = list(s)
print(t, type(t))

u = [7, 8, 9]
v = tuple(u)
print(v, type(v))

w = [1, 1, 2, 3]
x = set(w)
print(x, type(x))

y = [("key1", "value1"), ("key2", "value2")]
z = dict(y)
print(z, type(z))

aa = 1
bb = bool(aa)
print(bb, type(bb))

cc = 0
dd = bool(cc)
print(dd, type(dd))

ee = ""
ff = bool(ee)
print(ff, type(ff))

gg = 7
hh = complex(gg)
print(hh, type(hh))
