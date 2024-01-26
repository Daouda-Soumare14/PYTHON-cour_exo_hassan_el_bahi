liste = [i for i in range(5)]
m = [liste[i] for i in range(4, 0, -1)if liste[i] % 2 != 0]
print(m)

a = [1]
b = a
a[0] = 0
print(a)
print(b)
print(len(a))
print(len(b))

x = 3 % 1
y = 1 if x > 0 else 0
print(y)

def f(a, b):
    nom, denom = a, b
    def g():
        return nom/denom
    return g
a = f(1, 2)
b = f(3, 4)

f(a, b)

i = 5
while i > 0:
    i = i // 2   
    if i % 2 == 0:
        break
    else:
        i += 1
print(i)

# s = 'abc'
# for i in range(len(s)):
#     s[i] = s[i].upper()
# print(s)

for i in range(10):
    pass

t = (2, 3, 4)
t[:: 2]

print(t)
