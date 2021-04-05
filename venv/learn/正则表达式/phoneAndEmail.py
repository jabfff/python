#phoneAndEmail.py    find phone and email on the clipboard

import  re

pmFile = open('email.txt', 'r', encoding='utf-8')
emailFile = pmFile.read()

mo = emailRegex.findall(emailFile)

email.close()


#phone number regex
phoneRegex = re.compile(r'''(
    (\s|-|\.)?
    (\d{3}|(\d{4}))       #china area code
    (\s|-|\.)?              #symbol
    (\d{3,8})    #phone number
    (\s|-|\.)?              #symbol  
    (\d{1,5})?
    )''', re.VERBOSE)




print(mo)
# print(mo[0])
# print(mo[0][0])
for i in range(len(mo)):
    print(mo[i][0])


#email regex


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-] +       #user nanme
    @                        #symbol
    [A-Za-z0-9.-] +          #domain name
    (\.[a-zA-Z]{2,4})        #dot-email
    )''',re.VERBOSE)   #

