x="cos(10x)"
import math
def parsefunction(x):
    n=[]
    amp=0
    openbrackets=False
    sum=False
    offset=""
    freq=0
    for i in range(len(x)):
        cahr =x[i]
        if x[i].isnumeric() and openbrackets==False:
            if amp!=0:
                amp=(10*amp)+int(x[i])
                if x[i-2]=="-":
                    amp=amp*-1
            else:
                amp=int(x[i])
                if i!=0:
                    if x[i-1]=="-" and x[i+1].isnumeric()!=True:
                        amp=amp*-1
        elif x[i]=="c":
            if amp==0:
                amp=1
            function="cos"
        elif x[i]=="e":
            if amp==0:
                amp=1
            function="sen"
        elif x[i]=="(":
            openbrackets=True
        elif x[i]==")" and i!=len(x)-1:
            if freq==0:
                freq=1
            openbrackets=False
            sum=False
        elif x[i]=="p":
            if x[i-1].isnumeric():
                offset=3.14*int(x[i-1])
            else:
                offset=3.14
        elif x[i].isnumeric()==True and openbrackets==True and (x[i+1]=="x"):
            if freq!=0:
                freq=(10*offset)+int(x[i])
            else:
                freq=int(x[i])
        elif x[i]=='+' and openbrackets==True:
            sum=True
        elif x[i].isnumeric()==True and sum==True:
            if offset=="":
                offset=int(x[i])
            else:
                offset=(10*offset)+int(x[i])
        elif( (x[i]=="+" or x[i]=="-") and openbrackets==False) or (i==(len(x)-1)):
            if freq==0:
                freq=1
            n.append({"amp":amp,"freq":freq,"offset":offset,"function":function})
            num=0
            amp=0
            openbrackets=False
            sum=False
            offset=""
            freq=0
    print(n)
    return n
def num(x,function):
    table=[]
    for i in range(x):
        if function["offset"]=="":
            function["offset"]=0
        if function["function"]=="cos":
            y=math.cos(i*function["freq"]+function["offset"])*function["amp"]
            table.append(y)
        else:
            y=math.sin(i*function["freq"]*100+function["offset"])*function["amp"]

            table.append(y)
    return table    
def functionvalue(x,function):
    Table=[]
    results=[]
    result=0
    Results=[]
    for i in range(len(function)):
        table=num(x,function=function[i])
        Table.append(table)
    for i in range(x):
        for j in range(len(Table)):
            result=Table[j][i]+result
        results.append(result)
    for i in range(len(results)):
        Results.append(i)
        Results.append(results[i])
    return Results

n=parsefunction(x)
table=functionvalue(360,n)
print(table)
