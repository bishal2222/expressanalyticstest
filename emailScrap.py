import re , json
from collections import Counter

fileToRead = 'websiteData.txt'
fileTowrite = 'result.json'
delimiterInFile = [',', ';','. ']
#total email calculation
def validateEmail(strEmail):
    if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", strEmail):
        return True
    return False
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)


#find out type and occurance
def listofEmail(n):
    c1 = 0
    c2 = 0
    noOfEmail = []
    for i in n:
        if re.match("[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", i):
            c1 = c1 + 1
            d = i
            type1 = 'Non-Human'
        if re.match("[A-Za-z0-9]+[.][A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", i):
     
            c2 = c2 + 1
            e = i
            type2 = 'Human'
    a = dict([(f"{d}", dict([(f'Occurance' , c1) ,(f'EmailType', type1) ])), (f"{e}" , dict([(f'Occurance' , c2),(f'EmailType', type2)]))])
    # a = dict([(f'type', type1) , (f'Occurance' , c1)])
    noOfEmail.append(a)
    return a


#verifying result
b = listofEmail(listEmail)
print(b)
#writting in json format
file = open(fileTowrite, 'w')
json.dump(b, file) 






    



