from django.shortcuts import render#ibfn
from django.http import HttpResponse#cfn
import re#cfn

# Create your views here.
def homeone(request):
    responce = render(request,"home.html",)
    return responce

def reset(request):
    return render(request,"home.html",{'result':""})

def calculator(request):
    receivedinput = request.POST['calci']

    if receivedinput =="":
        return render(request,"home.html",{'result':""})

    fvalue = re.findall(r"(\d+)",receivedinput)# fvalue = Filterd values from receivedinput

    voperator = ['+','-','*','/','.','%']# voperator = variable operators

    foperator = []#after finished each loop function added (foperator =filterd operators) in empty list
        #print(foperator)#UPUP
        #UPUP = use PRINT function for understanding purpose only

    for ri in receivedinput:

        for vo in voperator:
            if ri == vo:
                foperator.append(vo)##UPUP append fn added the value in last (index or place) of foperator
                    #foperator#UPUP
                re.findall(r"(\d+)",receivedinput)##UPUP

        #initial speration part over, next match the operators
    for fo in foperator:
        if fo=='.':
            i = foperator.index(fo)#eg:opr=[55,2] <=> i=opr.index(2) <=> i=1 (i = index value)
            result1 = fvalue[i] + '.' + fvalue[i+1]#first operation done here, result data stored as a "result1"
            fvalue.remove(fvalue[i+1])#finished first operation filtervalue data Deleted here
            foperator.remove(foperator[i])#finished first operation filteroperator data Deleted here
            fvalue[i] = result1#result1 data  move to filtervalue using index operation
            #fvalue#UPUP
            #foperator#UPUP

    for fo in foperator:
        if fo == '%':
            i = foperator.index(fo)
            result1 = (float(fvalue[i])/100) * float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] = result1
            #fvalue#UPUP
            #foperator#UPUP

    for fo in foperator:
        if fo == '/':
            i = foperator.index(fo)
            result1 = float(fvalue[i]) / float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] = str(result1)
            #fvalue#UPUP
            #foperator#UPUP

    for fo in foperator:
        if fo == '*':
            i = foperator.index(fo)
            result1 = float(fvalue[i]) * float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] = str(result1)
            #fvalue#UPUP
            #foperator#UPUP

    for fo in foperator:
        if fo == '+':
            i = foperator.index(fo)
            result1 = float(fvalue[i]) + float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i]=str(result1)
            #fvalue#UPUP
            #foperator#UPUP

    for fo in foperator:
        if fo == '-':
            i = foperator.index(fo)
            result1 = float(fvalue[i]) - float(fvalue[i+1])
            fvalue.remove(fvalue[i+1])
            foperator.remove(foperator[i])
            fvalue[i] = str(result1)
            #fvalue#UPUP
            #foperator#UPUP


    if len(foperator) != 0:# ! = not equal
        if foperator[0] == '/':
            result2 = float(fvalue[0]) / float(fvalue[1])
        elif foperator[0] == '*':
            result2 = float(fvalue[0]) * float(fvalue[1])
        elif foperator[0]=='+':
            result2 = float(fvalue[0]) + float(fvalue[1])
        else:
            result2 = float(fvalue[0]) - float(fvalue[1])
    else:
        result2 = float(fvalue[0])

    result = round(result2,2)# round()function
    #result#UPUP
    responce = render(request,"home.html",{'result':result})
    return responce

""" Function example:

values= "55+66-3*6"
filter_value = re.findall(r"(\d+)",values)
print(filter_value) = ['55','66','3','6']

round()function
values= 5.5674
r=round(values,2)
print(r)= 5.57

"""


