# CS61002: Algorithms and Programming 1 
# Name: Manga Srinivas Rao Baipalli
# Date: 10/29/2016
# Lab: Project1.py

# Python program for Vocabulary quiz using files and dictionary. 


import random
import glob, os

# Initializing global variable
checkFlag=1
InputDict = {} #Initializing dictionary 
#InputFile = "wrong.txt" #wrong text file text stores into variable.

# Function to list the available files from Directory. 
def listingFiles():
    os.chdir(".") # Setting current directory 
    if (len(glob.glob('*.txt'))>0): 
        print("Select one of the following word lists:\n")
        print("Note: Choose verbs.txt vocabulary file for Quiz!\n")
        for file in glob.glob("*.txt"):
            print(file) #Printing the list of available files in current directory.        
        Main()
    else:
        print("ERROR: File(s) Not Found.")
        exit()
    
# Function to Open a Vocabulary file
def openFile(inputFileName):
    try:
        fopen = open(inputFileName,"r")
        return fopen
    except IOError as e:
        print("ERROR: File Not Found.")    
    
# Function to create dictionary and storing the keys and values from the Vocabulary text file in the form of Dictionary.
def randomKeys(inputFileName):
    fas = open(inputFileName,"r") #Calling openFile function 
    Dictionary_var = {} #Dictionary initialization
    for line in fas:
        #Dividing Keys and Values into ":" character.
        Dict_k, Dict_v = line.strip().split(':')
        Dictionary_var[Dict_k.strip()] = Dict_v.strip()
    fas.close()
    #Converting Dictionary into list to get the length of the diction in number.
    Dictionary_list = {key: list(map(str, value.split(','))) for key, value in Dictionary_var.items()}
    return Dictionary_list

# Function to take two inputs Filename and Dictionary to output missed words.
def FandD(InputDict, InputFile):
    try:
        wrongFile =open(InputFile, "a")
        with wrongFile as input_file:
            for Dict_k, Dict_v in InputDict.items():
                wrongWordsList = '{}: {}'.format(Dict_k, Dict_v)
                wrongFile.write(wrongWordsList+"\n") #Writing missed words from Dictionary to output file
        readWrong= open(InputFile,"r")
        print (readWrong.read()) #Reading missed words and printing them.
    except IOError as e:
        print("ERROR: File Not Found.")    
        exit()

# Function for repeating the process by doing looping  
def checkLoop():
    mark = input("\nDo you want to try again Y/N:")
    if (mark=='Y' or mark=='y'):
        checkFlag = 1
    elif (mark=='N' or mark=='n'):
        exit()
    else:
        print("Enter a number.")
        checkLoop() # Calling checkLoop function
        
# Function to write missed words into new file.          
def openAndWrite(InputFile):
    try:
        fopen = open("InputFile","a")
        fopen.writelines("")
        return fopen
        fopen.close()
    except IOError as e:
        print("ERROR: File Not Found.")    
        exit()
# Function to find number of words in a Vocabulary file.
def entriesFile(inputFileName):
    f_entries=0
    try:
        with open(inputFileName,"r") as f:
            for line in f:
                line.split()
                f_entries+=1
        return f_entries
    except IOError as e:
        print("ERROR: File Not Found.")
        exit()
# Main function 
def Main():
    # Variable initialization 
    flag=1
    correctCount = 0
    incorrectCount = 0
    while flag:
        inputFileName = input("Enter a file name:").lower()
        if(inputFileName == "verbs.txt" or inputFileName=="wrong.txt"):
            if(inputFileName == "verbs.txt"):
                print(entriesFile(inputFileName), " words found in a file." ) # calculating entries by calling file_entry() function
                if (entriesFile(inputFileName)>0):
                    checkFlag=1
                    while checkFlag:
                        how_many = input("How many words would you like to be quizzed on?:")
                        how_many = int(how_many)
                        if (entriesFile(inputFileName) >= how_many and how_many>0):
                            open("wrong.txt","w").close()#Closing wrong.txt file to erase content 
                            for i in range(how_many):
                                randomEnglishWord = random.choice(list(randomKeys(inputFileName).keys())) #Generating random english word.
                                spanish_word = (randomKeys(inputFileName)[randomEnglishWord]) #Getting Spanish word for the given english word.
                                print("\nEnglish word:",randomEnglishWord)
                                if (len(spanish_word)>1):
                                    print("You need to enter %d equivalent Spanish words."%(len(spanish_word))) 
                                    for i in range(len(spanish_word)):
                                        answer_input = input("Enter Spanish word %d:"%(i+1))
                                        if(spanish_word[i]==answer_input):
                                            Spanish_ans= True
                                        else:
                                            Spanish_ans= False
                                    if (Spanish_ans):
                                        print("-------")
                                        print("Correct")
                                        print("-------")
                                        correctCount+=1
                                        checkFlag=0
                                        flag=0
                                    else:
                                        print("---------")
                                        print("Incorrect")
                                        print("---------")
                                        InputDict[randomEnglishWord]=[spanish_word] #Pushing missed keys and values into new dictionary.
                                        incorrectCount+=1
                                        checkFlag=0
                                        flag=0    
                                else:
                                    print("You need to enter 1 equivalent Spanish word.")
                                    answer_input = input("Enter Spanish word:")
                                    if (answer_input == spanish_word[0]): 
                                        print("-------")
                                        print("Correct")
                                        print("-------")
                                        correctCount+=1
                                        checkFlag=0
                                        flag=0
                                    else:
                                        print("---------")
                                        print("Incorrect")
                                        print("---------")
                                        InputDict[randomEnglishWord]=[spanish_word]
                                        incorrectCount+=1
                                        checkFlag=0
                                        flag=0
                            print("\nRESULT:",correctCount, "out of", how_many)
                            if (correctCount==how_many):
                                print("Great! all answers are correct.")
                            else:
                                InputFile = input("Enter the file name to save missed words into file (Example: wrong.txt):").lower()
                                if (InputFile==""):
                                    print("ERROR: Invalid file.")
                                    exit()
                                else:
                                    print("The below missed words have been saved in %s file."%(InputFile))
                                    print()
                                    FandD(InputDict, InputFile) #calling FandD function to print missed words.
                        else:
                            print("ERROR: Invalid number.")
                            checkLoop()
                            flag=0
                else:
                    print("ERROR: Invalid file.")
                    exit()
            else:
                print("ERROR: Invalid file.\nEnter a valid vocabulary file name(Example: verbs.txt).\n")
                flag=1
        else:
            print("ERROR: Invalid file.\nEnter a valid vocabulary file name(Example: verbs.txt).\n")
            flag=1
print("----------------------------------------")
print("WELCOME TO THE VOCABULARY QUIZ PROGRAM.")
print("----------------------------------------\n")
listingFiles() #calling listingFlies() function to list the available files from directory.   