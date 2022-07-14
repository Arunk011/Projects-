'''Program:Ultimate Language Translation.
         Author:Arun Karthik
         Description:To create a new version of language translation using a data file. 
         Revisions:
         00-Defining the words with English and German words in a text file  
         01-Getting the list of word stored by opening the data file 
         02-User will enter the word in either English or German language 
         03-Adding the word if its not there in the respective lists
         04-Exiting the program and closing the File 
        '''

#Annoucement of the program 
print("Ultimate Language Translation")

translate = input("Program to translate words from English to German and vice-versa")

#Getting the words from the data file stored 
while True:
    English = []
    German = []

#Opening the Data File 
    with open('vocabulary.txt', 'r+') as f:
        data = f.readlines()
        for each in data:
            line = each.split()
            if len(line) == 2:
                English.append(line[0].lower())
                German.append(line[1].lower())
        f.close()
        
#User will enter the word either in English or German
    word = input("Enter an English or German word to translate : ")
    lowerWord = word.lower()
    print(lowerWord)
    if lowerWord in English:
        engIndex = English.index(lowerWord)
        print(f"The English word '{word}' is '{German[engIndex]}' in German.")

    elif lowerWord in German:
        GermanIndex = German.index(lowerWord)
        print(f"The German word '{word}' is '{English[GermanIndex]}' in English")

# Adding the word if its not in the above lists
    else:
        update = open('Vocabulary.txt', 'a+')
        addWord = input(f" The {word} in not found in the lists, Do you wish to add it ? Y/N : ")
        print(f'ENGLISH List: {English}')
        print(f'GERMAN List: {German}')
        write_data = ''
        if addWord.lower() == 'y':
            whichList = input(f"In Which list you want to add ? English/German  : ")
            if whichList.lower() == 'english':
                transWord = input(f"Enter the German Translation of this word '{word}' : ")
                update.writelines('\n')
                write_data = f'{lowerWord} {transWord} \n'
                print(write_data)
                update.writelines(write_data)

            elif whichList.lower() == 'german':
                tranword = input(f"Enter the English Translation of this word : {addWord}")
                write_data = f'{tranword} {lowerWord} \n'
                print(write_data)
                update.writelines('\n')
                update.writelines(write_data)
            update.close()

# Exiting the program
        else:
            break;
        
#Closing the File
        f.close()
