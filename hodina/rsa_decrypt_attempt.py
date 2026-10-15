# cislo = 275801

# for i in range(1,1000):
#     if cislo % i == 0:
#         print(ci
#

P = 73
Q = 71
F = (P - 1) * (Q - 1)
N = P * Q
B = 11

print((3619**2291)%N)
print((86**5)%1273)

k = 0
for k in range(1, F):
    A = (k * F + 1) / B
    if A - int(A) == 0:
        print(A)
        break
