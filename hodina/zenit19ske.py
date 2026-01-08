s = 13
i = input(f"pos (y x) (1-{s}) ").split()
y,x = int(i[0])-1,int(i[1])-1

if y == s-1 and x == s-1:
    print('Ujo je doma!')
else:
    som_pod_ujom = False
    print('#'*(s+2))
    for i in range(s-1):
        if i == y:
            som_pod_ujom = True
            print('#'+'.'*x+'U'+'x'*(s-x-1)+'#')
        elif som_pod_ujom:
            print(f'#{"."*(s-1)}x#')
        else:
            print(f'#{"."*s}#')
    if not som_pod_ujom:
        print('#'+'.'*(x)+'U'+'x'*(s-x-2)+'D#')
    else:
        print('#'+'.'*(s-1)+'D#')
    print('#'*(s+2))
