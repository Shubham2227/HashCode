from collections import *
from bisect import *

with open("c_incunabula.txt",'r') as files:
    Temp = files.readlines()
    n1=len(Temp)
    for _ in range(n1):
        Temp[_] = Temp[_].split()

    HashCodeBook,HashCodeLibrary,HashCodeDay = int(Temp[0][0]),int(Temp[0][1]),int(Temp[0][2])
    Div = Temp[1]
    Dictnory = {}
    for _ in range(HashCodeBook):
        Dictnory[_] = Div[_]
    Dictnory = OrderedDict(sorted(Dictnory.items(),key = lambda z:z[1],reverse = True))
    list_ = []
    for _ in Dictnory:
        list_.append(_)
    result = []
    total = 0
    for _ in range(2,2 * HashCodeLibrary + 2,2):
        B,C,D = set([*map(int,Temp[_ + 1])]),int(Temp[_][0]),int(Temp[_][1])
        HashCode_Library = int(Temp[_][2])
        result.append([C,D,HashCode_Library,B,total])
        total += 1
    result.sort(key = lambda z: z[1])
    stop = 0
    CountOfLibrary = 0
    listoflib,listofbook,listofTotal = [],[],[]
    for _ in range(HashCodeLibrary):
        Extra = False
        D = result[_][1]
        C = result[_][0]
        HashCode_Library = result[_][2]
        B = result[_][3]
        stop += D
        leftDays = HashCodeDay - stop
        leftDays *= HashCode_Library
        storeCount = result[_][4]
        if(stop > HashCodeDay):
            break
        else:
            list__ = []
            res = 0
            for _ in range(HashCodeBook):
                if(list_[_] in B):
                    list__.append(list_[_])
                    res += 1
                    if(res >= leftDays):
                        Extra = True
                        break
        CountOfLibrary += 1
        listofTotal.append(list__)
        listofbook.append(res)
        listoflib.append(storeCount)
        if(Extra):
            break
    with open("OutputFile.txt","w") as outputfile:
        outputfile.write(str(CountOfLibrary))
        outputfile.write("\n")
        for _ in range(CountOfLibrary):
            outputfile.write(str(listoflib[_])+" "+str(listofbook[_]))
            outputfile.write("\n")
            n=len(listofTotal[_])
            for index in range(n):
                if(index < n - 1):
                    outputfile.write(str(listofTotal[_][index])+" ")
                else:
                    outputfile.write(str(listofTotal[_][index]))
                    outputfile.write("\n")
