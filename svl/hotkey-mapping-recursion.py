file_id = 1
f = open(f"bt{file_id}.txt")
words = []
line = f.readline()
while line != "":
    words.append(line.strip())
    line = f.readline()
f.close()
words = sorted(words, key=len)


def find_char(w,chars):
    if w == []:
        print(chars)
        return

    word = w[0]
    for c in word:
        if not c in chars:
            find_char(w[1:],chars+c)


find_char(words,"")
