f = open("cisla.txt")
pocty = {"domace":0}
predvolby = {"420":"Cesko",
             "44":"Spojene Kralovstvo",
             }

for line in f:
    line = line.strip()

    if line[0:2:] == "09":
        pocty["domace"] += 1

    else:
        n = line[1:-9:]
        if n[0] == "0":
            n = n[1::]
        krajina = predvolby[n]

        if not krajina in pocty:
            pocty[krajina] = 0
        pocty[krajina] += 1

for key in pocty:
    print(f"{key} - pocet cisel: {pocty[key]}")

f.close()
