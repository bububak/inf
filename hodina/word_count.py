f = open("twain.txt")

text = f.read().strip().split()

d = {}
for word in text:
    word = word.lower()
    if not word in d:
        d[word] = 1
    else:
        d[word] += 1

l = []
for key in d:
    if d[key] > 10:
        l.append(key)

s = sorted(d.items(), key=lambda x:x[1], reverse=True)

for i in range(30):
    print(f"{s[i][0]}: {s[i][1]}")

f.close()
