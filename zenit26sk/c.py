def check_plate(ecv):
    if len(ecv) != 7:
        return "Nie"
    for i,c in enumerate(ecv):
        if str(i) in "234" and not c in "0123456789": # cislo
            return "Nie"
        if str(i) in "015678" and not c in "QWERTYUIOPASDFGHJKLZXCVBNM":
            return "Nie"
    return "Ano"



print(check_plate(input()))
