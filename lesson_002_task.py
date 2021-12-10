a = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

# sort by 2-th element
a1 = a.copy()
a1.sort(key = lambda x: x[1])
print(a1)

# create dict with key: 2-th element, values: other
a2 = {x[1]:x[:1]+x[2:] for x in a1 }
print(a2)

# sort values
a3 = {}
for k, v in a2.items():
    w = v.copy()
    w.sort(reverse=True)
    a3[k] = w
print(a3)

# create set from values
a4 = set(sum(a3.values(),[]))
print(a4)

# convert set to string
# a5 = str(a4)
a5 = ''.join(map(str,a4))
print(a5)

"""
# write output
f = open("Readme.md", "a")
f.write('# Lesson_002 task output\n')
f.write(str(a1)+'\\\n')
f.write(str(a2)+'\\\n')
f.write(str(a3)+'\\\n')
f.write(str(a4)+'\\\n')
f.write(str(a5))
f.close()
"""