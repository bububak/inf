n = int(input("Number of branches:\n> "))
width = 4+2*n
blank = " "
print(f"{(width//2-1)*blank}/\\{(width//2-1)*blank}\n{(width//2-1)*blank}##{(width//2-1)*blank}")
for i in range(n):
    print(f"{(width//2-i-3)*blank}{"#"*(i*2+6)}{(width//2-i-3)*blank}\n{(width//2-1)*blank}##{(width//2-1)*blank}")
print(f"{(width//2-2)*blank}/XX\\{(width//2-2)*blank}")
