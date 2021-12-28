f1 = "Fe2O3    +    3CO    →    2Fe    +    3CO2" #철 제련
f2 = "6CO2  +  6H2O    →    C6H12O6  +  6O2 " #광합성
f3 = "Cu  +  2Ag+  →   Cu2  +  2Ag" #은석출
f4 = "2Na  +  Cl2  →  2NaCl" #나트륨 연소반응

answer = input("f1:철제련\nf2:광합성\nf3:은석출\nf4:나트륨 연소반응\n: ")

if answer=="f1":
    print("철 제련: "+f1)
    a=input("입력: ")
    if a=="Fe2O3":
        print("Fe2O3:Fe2=6/O=-2")
    elif a=="3CO":
        print("3CO:C=2/O=-2")
    elif a== "2Fe":
        print("2Fe:Fe=0")
    elif a=="3CO2":
        print("3CO2:C=4/O=-4")
elif answer=="f2":
    print("광합성: "+f2)
    a=input("입력: ")
    if a=="6CO2":
        print("6CO2:C=4/O2=-4")
    elif a=="6H2O":
        print("6H2O:H2=2/O=-2")
    elif a=="C6H12O6":
        print("C6H12O6:C6=0/H12=12/O6=-12")
    elif a=="6O2":
        print("6O2:O2=0")
elif answer=="f3":
    print("은 석출: "+f3)
    a=input("입력: ")
    if a=="Cu":
        print("Cu:Cu=0")
    elif a=="2Ag+":
        print("2Ag+:Ag+=1")
    elif a=="Cu2":
        print("Cu2:Cu2=0")
    elif a=="2Ag":
        print("2Ag:Ag=0")
elif answer=="f4":
    print("나트륨 연소반응: "+f4)
    a=input("입력: ")
    if a=="2Na":
        print("2Na:Na=0")
    elif a=="Cl2":
        print("Cl2:Cl2=0")
    elif a=="2NaCl":
        print("2NaCl:Na=1/Cl=-1")
