n = int(input("Number of branches:\n> "))
width,blank = 4+2*n+2, " "
print(f"{(width//2-1)*blank}/\\\n{(width//2-1)*blank}##")
for i in range(n):
    print(f"{(width//2-i-3)*blank}{"#"*(i*2+6)}")
    print(f"{(width//2-i-3)*blank}",end="")
    print((i+2)//2*"o ",end="")
    print(f"{" "*((i+2)%2)}##",end="")
    print(f"{" "*((i+2)%2)}",end="")
    print((i+2)//2*" o")
print(f"{(width//2-1)*blank}##\n{(width//2-2)*blank}/XX\\")
