s = input("Your Message:\n")

state = False  # -1=male 1=velke
o = ""  # output string


for i, c in enumerate(s):
    if c == " ":  # state swap
        state = not state

    else:
        if state:  # ak menim na velke
            if "A" <= c <= "Z":
                o += c
            elif "a" <= c <= "z":
                o += chr(ord(c) - 32)
            else:
                o += c

        elif not state:  # ak menim na male
            if "a" <= c <= "z":
                o += c
            elif "A" <= c <= "Z":
                o += chr(ord(c) + 32)
            else:
                o += c


print(o)
