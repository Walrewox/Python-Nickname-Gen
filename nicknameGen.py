import random

""" 1) Enter your full name or other words, from which you would like to form a nickname"""
real = "Kreative Oblivion"
""" 2) Do this again for more variability! """
pseudo = "Awesome Perspective"

file = open('nicknames.txt','w')
rows = 1000
while rows > 0:
    columns = 4
    while columns > 0:
        lenght = 8
        while lenght >= 0:
            """
            If the first 3 columns are formed,
            then the letters are taken from the first variable.
            """
            if columns > 2:
                file.write(real[random.randint(0,len(real)-1)])
                """ Else from second variable """
            else:
                file.write(pseudo[random.randint(0,len(pseudo)-1)])
            lenght -= 1
        file.write('    ')
        columns -= 1
    file.write('\n')
    rows -= 1
file.close()
""" 3) Open nicknames.txt, find the nick or improve one of the sets of words and use! """
