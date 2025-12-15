f = input("enter brackets: ")
stack = []
pairs = {')':'(',']':'[','}':'{'}
check = True
for i in range(len(f)):
    c = f[i]
    if c in '([{':
        stack.append(c)
    if c in ')]}':
        if len(stack) == 0:
            check = False
            break
        if stack[-1] == pairs[c]:
            stack.pop()
        else:
            check = False
            break
if len(stack) == 0 and check:
    print('correct')
else:
    print('invalid input')
