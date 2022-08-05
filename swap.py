str1='abc'
str2='xyz'
temp=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],temp)
print(str1,end=' ')
print(str2)
     