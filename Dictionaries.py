tel = {'jack': 4098, 'bob': 4139}
print("Initial tel:", tel)

tel['pluto'] = 4127
print("After adding pluto:", tel)

print("Value for 'pluto':", tel['pluto'])

del tel['bob']
tel['raj'] = 4127
print("After deleting 'bob' and adding 'raj':", tel)

print("List of keys:", list(tel))
print("Sorted keys:", sorted(tel))

print("'pluto' in tel:", 'pluto' in tel)
print("'pluto' not in tel:", 'pluto' not in tel)
