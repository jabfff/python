import  re, os



emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-] +       #user nanme
    @                        #symbol
    [A-Za-z0-9.-] +          #domain name
    (\.[a-zA-Z]{2,4})        #dot-email
    )''',re.VERBOSE)   #


email = open('email.txt', 'r', encoding='utf-8')
emailFile = email.read()

mo = emailRegex.findall(emailFile)

email.close()


print(mo)
# print(mo[0])
# print(mo[0][0])
for i in range(len(mo)):
    print(mo[i][0])