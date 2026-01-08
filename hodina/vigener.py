def encode(word,key):
    out = ""
    for i in range(len(word)):
        c_i = alphabet.find(word[i])
        key_i = alphabet.find(key[i%len(key)])
        out += alphabet[(c_i+key_i)%len(alphabet)]
    return out


def decode(word,key):
    out = ""
    for i in range(len(word)):
        c_i = alphabet.find(word[i])
        key_i = alphabet.find(key[i%len(key)])
        out += alphabet[(c_i-key_i+len(alphabet))%len(alphabet)]
    return(out)

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_word = input("Enter Phrase: \n> ")
input_key = input("Enter Key: \n> ")

print("-"*10)

print(f"Decoded Phrase: \n{decode(input_word, input_key)}")
print(f"New Phrase: \n{encode(input_word, input_key)}")
