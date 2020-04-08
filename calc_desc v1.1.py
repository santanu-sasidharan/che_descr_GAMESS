#logfile
file = open("log.txt", 'w')
#Input homo and lumo values
while True:
    try:
        e_lumo = float(input("Enter LUMO  value = "))
    except ValueError:
        print("Please enter a number! Try again.")
        continue
    else:
        break
while True:
    try:
        e_homo = float(input("Enter HOMO value = "))
    except ValueError:
        print("Please enter a number! Try again.")
        continue
    else:
        break

#covert HE to ev
convert = input("Do you want to convert HE to eV? y/n ")
if convert == "y":
    e_lumo = (e_lumo*27.2114)
    e_homo = (e_homo*27.2114)
elif convert == "n":
    print("Calculating .....")

#Define function
#Ionizaition potential (IP)
def ip(x):
    IP = (-x)
    file.write("Ionisation potential(IP) = " + "%.2f" %IP + " eV" + '\n')

#Electron affinity (EA)
def ea(x):
    EA = (-x)
    file.write("Electron Affinity (EA) = " + "%.2f" %EA + " eV" + '\n')
    return EA

#Energy Gap (EG)
def eg(x, y):
    EG = abs(x-y)
    file.write("Energy Gap (EG) = " + "%.2f" %EG + " eV" + '\n')
    return EG

#Electronegativity (EN)
def en(x, y):
    EN = (-(x+y)/2)
    file.write("Electronegativity (EN) = " + "%.2f" %EN + " eV" + '\n')
    return EN

#Chemical Potential (CP)
def cp(x, y):
    CP = ((x+y)/2)
    file.write("Chemical potential (CP) = " + "%.2f" %CP + " eV" + '\n')
    return CP

#Chemical Hardness (CH)
def ch(x, y):
    CH = ((abs(x-y)/2))
    file.write("Chemical Hardness (CH) = " + "%.2f" %CH + " eV" + '\n')
    return CH

#Chemical softness (CS)
def cs(x, y):
    CS = (1/((abs(x-y))))
    file.write("Chemical Softness (CS) = " + "%.2f" %CS + " eV" + '\n')
    return CS

#Electrophilicity index (EI)
def ei(x, y):
    EI = (x**2/(2*y))
    file.write("Electrophilicity index (EI) = " + "%.2f" %EI + " eV" + '\n')

#Call for functions
file.write("HOMO = " + "%2f" %e_homo + " eV" + '\n')
file.write("LUMO = " + "%2f" %e_lumo + " eV" + '\n')
ip(e_homo)
ea(e_lumo)
eg(e_lumo, e_homo)
en(e_lumo, e_homo)
cs(e_lumo, e_homo)
ei(cp(e_lumo, e_homo), ch(e_lumo, e_homo))
file = open("log.txt", 'r')
print (file.read() )
print("Done. Please check the log file")
file.close()

