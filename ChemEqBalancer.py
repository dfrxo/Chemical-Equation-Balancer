# Only works for the decomposition of two elements :)

# Ion charges of ion elements
# chemDict = {"Cl":-1,"F":-1,"Br":-1,"I":-1,"At":-1,
#             "O":-2,"S":-2,"Se":-2,"Te":-2,
#             "N":-3,"P":-3,"As":-3,
#             "C":4,"Si":4,
#             "B":3,
#             "Be":2,"Mg":2,"Ca":2,"Sr":2,"Ba":2,"Ra":2,
#             "H":1,"Li":1,"Na":1,"K":1,"Rb":1,"Cs":1,"Fr":1,
            
#             "Fe3+":3,"Au3+":3,
#             "Zn":2,"Cd":2, "Cu2+":2,"Ni":2,"Fe2+":2,"Mn":2,
#             "Cu":1,"Ag":1,"Au":1}

# plusOne = {"H":1,"Li":1,"Na":1,"K":1,"Rb":1,"Cs":1,"Fr":1}
# plusTwo = {"Be":2,"Mg":2,"Ca":2,"Sr":2,"Ba":2,"Ra":2}

# minusTwo = {"O":-2,"S":-2,"Se":-2,"Te":-2}

from sympy import symbols, Eq, solve

# Unbalanced Equation Cases
input = "Li+F2=LiF"
# input = "H2+Cl2=HCl"
# input = "Mg+Br2=MgBr2"
# input = "Li+F2=LiF"
# input = "H2+O2=H2O"


x = symbols('x')

print(input)
leftRight = input.split("=")
leftSide = leftRight[0].split("+")
i = ""
el = ""
flag = False
rightDict = {}
leftDict = {}
sepList = []
count = 0
for element in leftSide:
    for i in element:
        if i.isdigit():    
            num = int(i)
            leftDict.update({el:num})
            sepList.append(el)
            el = ""
            num = 1
        else:
            el = el + i
            if i == element[len(element)-1][-1]:
                leftDict.update({element:1})
                sepList.append(el)
                el=""
                i=""
for i in leftRight[1]:
    if flag:
        flag = False
        continue
    if i.isdigit():    
        num = int(i)
        rightDict.update({el:num})
        #sepList.append(el)
        el = ""
        num = 1
    else:
        el = el + i
        if i == leftRight[len(leftRight)-1][-1]:
            rightDict.update({el:1})
            #sepList.append(el)
        try:
            if ord(leftRight[1][leftRight[1].index(i)+1]) < 91:
                if  leftRight[1][leftRight[1].index(i)+1].isdigit():
                    rightDict.update({el:int(leftRight[1][leftRight[1].index(i)+1])})
                else:
                    rightDict.update({el:1})
                    el = ""
                    continue
                #rightDict.update({el:1})
                flag = True
                el = ""
                
                
        except Exception:
            pass  


coEff_1 = leftDict[sepList[0]]
rightCoEff_1 = rightDict[sepList[0]]
coEff_2 = leftDict[sepList[1]]
rightCoEff_2 = rightDict[sepList[1]]


while coEff_1 != rightCoEff_1 or coEff_2 != rightCoEff_2:
    while coEff_1!=rightCoEff_1:
        if coEff_1 < rightCoEff_1:
            equation = Eq(x * coEff_1, rightCoEff_1)
            sol = solve(equation)
            num = sol[0]
            coEff_1 = coEff_1 * num
        else:
            equation = Eq(x * rightCoEff_1, coEff_1)
            sol = solve(equation)
            num = sol[0]
            rightCoEff_2 = rightCoEff_2 * num
            rightCoEff_1 = rightCoEff_1 * num
    while coEff_2 != rightCoEff_2:
        if coEff_2 < rightCoEff_2:
            equation = Eq(x * coEff_2, rightCoEff_2)
            sol = solve(equation)
            coEff_2 = coEff_2 * sol[0]
        else:
            equation = Eq(x * rightCoEff_2, coEff_2)
            sol = solve(equation)
            num1 = sol[0]
            rightCoEff_2 = rightCoEff_2 * num1
            rightCoEff_1 = rightCoEff_1 * num1



if coEff_1 != leftDict[sepList[0]]:
    coEff_1 /= leftDict[sepList[0]]
    coEff_1 = str(coEff_1)
else:
    coEff_1 = ""
if coEff_2 != leftDict[sepList[1]]:
    coEff_2 /= leftDict[sepList[1]]
    coEff_2 = str(coEff_2)
else:
    coEff_2 = ""
if rightCoEff_1 != rightDict[sepList[0]]:
    rightCoEff_1 /= rightDict[sepList[0]]
    rightCoEff_1 = str(rightCoEff_1)
else:
    rightCoEff_1 = ""

i=0
for key in leftDict:
    if leftDict[key]>1:
        sepList[i] += str(leftDict[key])
    i+=1    

print(coEff_1 + sepList[0] + "+" + coEff_2 + sepList[1] + "=" + rightCoEff_1 + leftRight[1])