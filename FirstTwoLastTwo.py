str=raw_input("Enter the string!!")
if(len(str)==1):
    out=""
else:
    out=str[0]+str[1]+str[len(str)-2]+str[len(str)-1]
print out