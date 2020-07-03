import random

real = "Kukotin Oleksandr"
pseudo = "Pavlyuk Aleksandr"

file = open('nicknames.txt','w')
count = 0
while count < 100:
    size = 8
    columns = 6
    while columns > 0:
        size = 8
        while size >= 0:
            if columns > 3:
                file.write(real[random.randint(0,16)])
            else:
                file.write(pseudo[random.randint(0,16)])
            size -= 1
        file.write('    ')
        columns -= 1
    file.write('\n')
    count += 1
file.close()
