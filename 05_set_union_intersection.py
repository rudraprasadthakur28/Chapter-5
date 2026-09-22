s1 = {1, 22, 3, 8}
s2 = {20, 1, 269, 458, 235}

print(s1.union(s2))
print(s1.intersection(s2))

print({1, 22}.issubset(s1))
print(s1.issuperset({1, 22}))