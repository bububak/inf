# print([n**2 for n in range(1,101)])
#
# print([chr(n) for n in range(97,123) if chr(n) not in "aeiou"])
#
# with open("twain.txt") as f:
#     print([slovo for slovo in f.read().split() if len(slovo) == 8])
#
# with open("twain.txt") as f:
#     print([slovo for slovo in f.read().split() if "x" in slovo])
#
# with open("twain.txt") as f:
#     print(set([slovo for slovo in f.read().split() if "x" in slovo]))
#
# with open("twain.txt") as f:
#     print(len(set([slovo for slovo in f.read().split() if "x" in slovo])))

chaos = (1,0,17.3,18,2,2.1234,"63","21.3","vybostok@gjh.sk","ahoj","4hoj",True,"False")

print([item for item in chaos if type(item) == float])
