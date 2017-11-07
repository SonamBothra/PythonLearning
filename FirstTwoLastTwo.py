str=raw_input("Enter the string!!")
if(len(str)==1):
    out=""
else:
    out=str[:2]+str[-2:]
print out