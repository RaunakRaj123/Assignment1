name='restart'
namem=name[0]
y='r'
x=len(name)
for char in range(1,len(name)):
    if y==name[char]:
        namem+='$'
    else:
       namem+=name[char]
    char+=1   
print(namem)  