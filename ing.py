t=1
while t>-1:
    string1=input("Enter a string: ")
    str1='ing'
    l=len(string1)
    if l>3:
      if string1[l-3:l]==str1:
        print(string1+'ly')
      else:
        print(string1+'ing')
    else:
      print(string1)
t-=1   
