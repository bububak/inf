num_of_loops = int(input())

for i in range(num_of_loops):
    bez_nul = bin(int(input()))[1:]
    otocene = ""
    for i in range(len(bez_nul)-1,0,-1):
        otocene += bez_nul[i]
    otocene += "0" * (32 - len(otocene))
    print(int(otocene,2))
