# making list from file and closing
file_id = 1
f = open(f"bt{file_id}.txt")
words = []
ci = []
chars = []
line = f.readline()
while line != "":
    words.append(line.strip())
    chars.append("")
    ci.append(0)
    line = f.readline()
f.close()
words = sorted(words, key=len)


# check ktory pozrie ci mame viac originalnych pismen ako slov


# wi = current word index
# ci = list of which character index the words are set as
# chars = list of output chars
# ci[wi] = pos of current characteer for word at index wi

print(words)

wi = 0
while wi < len(words):
    word = words[wi]
    for i in range(ci[wi],len(word)):
        c = word[i]
        if not c in chars:
            chars[wi] = c
            ci[wi] = i

            wi += 1
            break
    else:
        chars[wi] = ""
        ci[wi] = 0
        wi -= 1





# printing output
for i in range(len(words)):
    print(f"{ci[i]}, {chars[i]} - {words[i]}")
