def FindMaxLengthStr(strList):
    maxLength=0;
    outStr=""
    for str in strList:
        if(len(str)>maxLength):
            maxLength=len(str)
            outStr=str
    return outStr
def find_longer_than_n(input_list, length):
    outList=[]
    for str in input_list:
        if (len(str) > length):
            outList.append(str)
    return outList
def add_tags(tag_name,tag_body):
    return '<'+tag_name+'>'+tag_body+'</'+tag_name+'>'
inputList=['data','variable','python','oops','interpreter','compiler','inheritance']
maxLengthName=FindMaxLengthStr((inputList))
outlist=find_longer_than_n(inputList,4)
html_tag=add_tags('i','python')
print maxLengthName
print outlist
print html_tag