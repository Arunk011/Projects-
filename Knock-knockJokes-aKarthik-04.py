'''Program:Knock-knock Jokes  
         Author:Arun Karthik
         Description: A knock-knock joke is a highly structured dialog between a joke teller and a willing participant  .
         Revisions:
         00-Importing the Random Module 
         01-Removing the punctuation  
         02-Converting the response to lower case and shuffling them
         03- Creating the list to store the jokes 
         04- Displaying the Jokes
        '''

#Importing the Random Module 
import random

#We have to remove the unwanted characters from the response 
def cleanData(str_data):
    str_data = str_data.lower()

# Removing punctuation
    punctuation = "!@#$%^&*()_+<><>,.:'?"
    for each in str_data:
        if each in punctuation:
            str_data = str_data.replace(each, '')
    return str_data.strip()

def knock_knock():
    print(f'-----------------------Knock Knock Jokes----------------------------')
    print("Knock Knock")
    userInput = input()

# Converting all the response to lowercase and shuffling the jokes 
    res = [cleanData(i) for i in userResponse]

    if cleanData(userInput) in res:
        random.shuffle(jokes_data)
        shuffleword = jokes_data[0]
        print(shuffleword[0])
        punchlineResp = input()
        if cleanData(punchlineResp) == cleanData(shuffleword[0] + ' who'):
            print(shuffleword[1])
        else:
            print(f'you need to say "{shuffleword[0]} who?" \n')
    else:
        print('''Sorry.The correct response is "Who's there?" Try again.''')
    print('\n')


# Creating a list to store the Jokes along with the punchlines. 

jokes_data = [['Etch', "Please sneeze into your elbow!"],
        ["cash", "No I prefer peanuts"],
        ['Dwayne', "Dwayne the tub before I dwown"],
        ["Boo", "Don't cry, it’s only a joke"],
        ["Ya", "I’m happy to see you too!"],
        ["Tank", "You’re welcome."]]


userResponse = ["who's there ?", "who is there"]

#Asking the user to print how many number of Jokes they want 

print(f'we have {len(jokes_data)} number of jokes')
print(f'-----------------------Knock Knock Joke----------------------------\n')
njokes = input("Enter the number of jokes you want to hear")

#To compare the number of jokes available and number of jokes the user wants
if njokes.isdigit():
    if int(njokes) > len(jokes_data):
        print(f"We have only {len(jokes_data)} jokes , please enter a value less than or equal to {len(jokes_data)}")
    for i in range(0, int(njokes)):
        knock_knock()
else:
    print("Please Enter a numeric value !")

#Exit with an appropriate, cheerful, and affirmative message   
print("Thanks for playing! Have a Wonderful day!")
