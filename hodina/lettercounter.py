def print_result():
    for i in range(len(chr_counter)):
        if chr_counter[i] != 0:
            print(f"{chr(i + 97)}: {chr_counter[i]}")


def get_input():
    # return input("Your Input: ").strip()
    f = open("countingtext.txt")
    return f.read()


def count_alphabet_only():
    for i in range(len(input_string)):
        n = ord(input_string[i])

        if n >= 65 and n <= 90:
            n += 32

        if chr(n) in "i" and chr(ord(input_string[i + 1])) in "aeu":
            chr_counter[ord(input_string[i + 1]) - 97] -= 1
            chr_counter[ord("i") - 97] -= 1
        if n >= 97 and n <= 122:
            chr_counter[n - 97] += 1


input_string = get_input()
chr_counter = [0] * 26


count_alphabet_only()
print_result()
