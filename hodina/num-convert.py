def base_convert(original, base_input, base_output):

    # anything to decimal
    n = 0
    v = 1
    o = str(original)
    for i in range(len(o)):
        n += int(o[-(i+1)])*v
        v *= base_input

    # decimal to anything
    out = ""
    while n:
        rest = n % base_output
        n = n // base_output
        out = str(rest) + out
    return int(out)


print(base_convert(1101, 2, 5))
