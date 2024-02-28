String = 'This is {} python training%$ {}'
# conv = String.lower()
# print(conv)
# conv = String.casefold()
# print(conv)
print(String[2:6]) # print is is python training%$
print(String[8])
print(String.count('n'))
print(String.format('My','session'))

'''
for i in range(4,len(String)):
    print(String[i])
'''
# conv = String.split()[-4]
# print("String revers",conv)

# Num='123456'
# x= Num.isdigit()
# y= Num.isnumeric()
# print(x)
# print(y)


txt = "   Hello world  "
print(txt[2:5])
print(txt.strip())

def greet(no):
   print(f"hello",{no})

greet(int(input("Enter: ")))
