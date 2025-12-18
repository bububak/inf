
n = int(input("Number of branches:\n> "))
width = 4+2*n+2
blank = " "

#     /\
#     ##
#  ~? ## ?~
#   ######
#   ######
#     ##
# ~?  ##  ?~
#  ########
#  ########
#     ##
#     ##
#    /XX\

# top of tree
print(f"{(width//2-1)*blank}/\\\n{(width//2-1)*blank}##")

# cycle for branch + trunk under
for i in range(n):
    # print(f"{(width//2-i-3)*blank}{"#"*(i*2+6)}\n{(width//2-1)*blank}##")
    print(f"{(width//2-i-4)*blank}~?{blank*(i+1)}##{blank*(i+1)}?~")
    print(f"{(width//2-i-3)*blank}{"#"*(i*2+6)}")
    print(f"{(width//2-i-3)*blank}{"#"*(i*2+6)}")
    print(f"{(width//2-1)*blank}##")

# bottom of trunk
print(f"{(width//2-1)*blank}##")
print(f"{(width//2-2)*blank}/XX\\")
