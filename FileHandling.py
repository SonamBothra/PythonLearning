#Reading from the file
handle=open("Data.txt",'r')
lines=handle.readlines()
print(lines)
handle.close()

#with keyword takes care of automatically closing the file handle
with open("Data.txt",'r') as f:
    content=f.readlines()
    print(content)

#Writing the read data to the file
newfile=open("new.txt","w")
newfile.write("This is the first line")
for each in lines:
    newfile.write(each)