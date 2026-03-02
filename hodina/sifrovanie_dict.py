with open("desif_tabulka.txt", encoding="UTF-8") as f:

    d = {}
    entered_brackets = False
    for line in f:
        l = line.strip()
        i = 0
        while i < len(line):
            c = line[i].lower()
            if c == "{":
                entered_brackets = True
            elif c == "}":
                entered_brackets = False

            if c.isalpha():
                if entered_brackets:
                    if line[i+2] == ":":
                        d[c] = line[i+5]
                        i += 5
            i += 1

with open("sub_sifra.txt", encoding="UTF-8") as f:
    for line in f:
        l = line.strip()
        for i,c in enumerate(l):
            if c.isalpha():
                print(d[c.lower()],end="")
            else:
                print(c, end="")

reversed_d = {}
for key in d:
    reversed_d[d[key]] = key

print()
print()
text_to_encode = "marek"
for c in text_to_encode:
    if c.isalpha():
        print(reversed_d[c],end="")
    else:
        print(c,end="")
