# imports all the nessaserry functions 
from pandas import read_csv
from random import randint, randrange


def csvReader ():

    # generates the 3 numbers for the csv file
    ran = [randrange (0, 423964) for i in range (3)]
    # makes the csv into a table 
    global dataFrame
    dataFrame = read_csv ("pass.csv")
    
    #chooses the word depending on the row there in
    wordOne = dataFrame.iloc[ran, 1].values[0]
    wordTwo = dataFrame.iloc[ran, 1].values[1]
    wordThree = dataFrame.iloc[ran, 1].values[2]
    
    global capWordOne
    global capWordTwo
    global capWordThree
    capWordOne = str.capitalize(wordOne)
    capWordTwo = str.capitalize(wordTwo)
    capWordThree = str.capitalize(wordThree)

    


def filler ():
    acceptance = input ("does this password work well for you? Please input 'YES' or 'NO' \n\n")
    if acceptance == 'YES':

        # asks the user if the program worked or not
        yesOrNo = input ("\nIs the program working correctly if so enter 'YES' "
                        "else enter 'NO' \n\n")
        done = False
        while done != True:

            if yesOrNo == "YES":
                print ("\n~~~~~~~~~~~~~~~~~~\n")
                print ("Program as ended")
                print ("\n~~~~~~~~~~~~~~~~~~")
                done = True

            elif yesOrNo == "NO":
                print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print ("This will print the csv and check that the random number generator,"
                    "in the correct value compared to the last csv row out puted on the terminal \n")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
                print (dataFrame)
                break

            else:  
                print ("Enter either 'YES'/'NO' \n")
                break

    elif acceptance == 'NO':
        csvReader()
        passGen()
        filler()

    else:
        filler()


def passGen ():
    
    randomNum = randint (1000, 9999)
    #converting int to string
    strRandomNum = str(randomNum)
    
    listRandom = randint (0, 20)
    list = ["!", "£", "$", "€", "%", "^", "&", "*", "(", ")",
            ",", ".", "<", ">", "/", "?", "'", "@", "#", "~"]
    
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print (capWordOne + capWordTwo + capWordThree + strRandomNum + list[listRandom])
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    

    

csvReader()
passGen()
filler()