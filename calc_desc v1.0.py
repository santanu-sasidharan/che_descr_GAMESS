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
    print("Ionisation potential(IP) = " + "%.2f" %IP + " eV")

#Electron affinity (EA)
def ea(x):
    EA = (-x)
    print("Electron Affinity (EA) = " + "%.2f" %EA + " eV")
    return EA

#Energy Gap (EG)
def eg(x, y):
    EG = abs(x-y)
    print("Energy Gap (EG) = " + "%.2f" %EG + " eV")
    return EG

#Electronegativity (EN)
def en(x, y):
    EN = (-(x+y)/2)
    print("Electronegativity (EN) = " + "%.2f" %EN + " eV")
    return EN

#Chemical Potential (CP)
def cp(x, y):
    CP = ((x+y)/2)
    print("Chemical potential (CP) = " + "%.2f" %CP + " eV")
    return CP

#Chemical Hardness (CH)
def ch(x, y):
    CH = ((abs(x-y)/2))
    print("Chemical Hardness (CH) = " + "%.2f" %CH + " eV")
    return CH

#Chemical softness (CS)
def cs(x, y):
    CS = (1/((abs(x-y))))
    print("Chemical Softness (CS) = " + "%.2f" %CS + " eV")
    return CS

#Electrophilicity index (EI)
def ei(x, y):
    EI = (x**2/(2*y))
    print("Electrophilicity index (EI) = " + "%.2f" %EI + " eV")

#Call for functions
print("HOMO = " + "%2f" %e_homo + " eV")
print("LUMO = " + "%2f" %e_lumo + " eV")
ip(e_homo)
ea(e_lumo)
eg(e_lumo, e_homo)
en(e_lumo, e_homo)
cs(e_lumo, e_homo)
ei(cp(e_lumo, e_homo), ch(e_lumo, e_homo))


