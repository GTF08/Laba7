import codecs
#Собирает словарь из букв и их частот по убыванию
def MakeFreqDictionary(filepath, isRus):
    outDict = dict()
    if(isRus):
        #Открытие файла простым open Не работало
        opFile = codecs.open(filepath, 'r',"utf_8_sig" )
    else:
        opFile = open(filepath, 'r')
    for line in opFile:
        for char in line:
            if(char in outDict):
                outDict[char] = outDict[char]+1
            else:
                outDict[char] = 1

    opFile.close()
    return dict(reversed(sorted(outDict.items(), key = lambda item: item[1])))

#Замена символа зашифрованного текста на символ той же частоты незашифрованного
def ChangeChar(char,charFreq, encrFreq):
    charFreqList = list(charFreq)
    encrFreqList = list(encrFreq)

    return charFreqList[encrFreqList.index(char)]

#Функция для попытки частотной дешифровки
def FreqDecrypt(filepath, charFreq, encrFreq):
    opFile = open(filepath, 'r')
    writeFile = open("FreqDecrypted.txt", 'w')

    for line in opFile:
        resultLine = ""
        for char in line:
            resultLine += ChangeChar(char,charFreq,encrFreq)

        writeFile.write(resultLine)
        
    opFile.close()
    writeFile.close()

#Моя попытка ручной дешифровки текста. Результат удачный - шифр Цезаря, поворот 19
def TryDecrypt(filepath):
    opFile = open(filepath, 'r')
    writeFile = open("result.txt", 'w')

    for line in opFile:
        resultLine = ""
        
        for char in line:
            addchar = ''
            char = char.lower()
            
            if char == 'х':
                addchar = 'г'
        
            if char == 'б':
                addchar = 'о'
                
            if char == 'ц':
                addchar = 'д'
                
            if char == 'ё':
                addchar = 'у'
                
            if char == 'ы':
                addchar = 'и'
                
            if char == 'р':
                addchar = 'ю'
                
            if char == 'с':
                addchar = 'я'
                
            if char == 'ф':
                addchar = 'в'

            if char == 'й':
                addchar = 'ч'
                
            if char == 'т':
                addchar = 'а'
                
            if char == 'д':
                addchar = 'с'
                
            if char == 'в':
                addchar = 'п'
                
            if char == 'ю':
                addchar = 'л'

            if char == 'ч':
                addchar = 'е'

            if char == 'г':
                addchar = 'р'

            if char == 'а':
                addchar = 'н'

            if char == 'щ':
                addchar = 'ж'

            if char == 'н':
                addchar = 'ы'

            if char == 'ъ':
                addchar = 'з'

            if char == 'е':
                addchar = 'т'

            if char == 'у':
                addchar = 'б'
                
            if char == 'о':
                addchar = 'ь'

            if char == 'я':
                addchar = 'м'

            if char == 'э':
                addchar = 'к'

            if char == 'з':
                addchar = 'х'

            if char == 'л':
                addchar = 'щ'

            if char == 'к':
                addchar = 'ш'

            if char == 'п':
                addchar = 'э'

            if char == 'ь':
                addchar = 'й'

            if char == 'и':
                addchar = 'ц'

            if char == 'ж':
                addchar = 'ф'
                
            if(addchar ==''):
                addchar = char
            
            resultLine += addchar
                
        print(resultLine)
        writeFile.write(resultLine)
        
    opFile.close()
    writeFile.close()

#путь к файлу на русском языке                
rusFilePath = "rus.txt"
#путь к файлу зашифрованному
encrFilePath = "4-1.txt"


rusFreq = MakeFreqDictionary(rusFilePath,True)
encrFreq = MakeFreqDictionary(encrFilePath, False)


#TryDecrypt("4-1.txt")
#ROT-19
FreqDecrypt(encrFilePath,rusFreq, encrFreq)



