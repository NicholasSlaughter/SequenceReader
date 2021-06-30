import sys
import os
import fileinput

class Helper(object):
    #This class is used to get rid of redundences and make large code blocks easier to read

    #If a sequence is new it will be added to the dictionary. If a dictionary is not new it will have its value incremented by 1
    def Add_To_Dictionary(seq,seq_dict):
        #If the sequence is not in the dictionary then add it with the value of 0
        if seq not in seq_dict:
            seq_dict[seq]=0
        seq_dict[seq]+=1 #increment the value of the sequence by 1 
        return seq_dict[seq] #return the dictionary

    #Checks to see which stream of files is needed for a given instance
    #If we are testing then we run the test files otherwise we run the files specified from the command line
    def Input_Check(files):
        if files: #if test files are passed then run the test files (Used fileinput.FileInput(files) because if all tests were ran at once some would fail and say that input() was already in use)
            return fileinput.FileInput(files)
        elif len(sys.argv) > 1 or not sys.stdin.isatty(): #There are commands from the command line so lets run them
            return fileinput.input() #If fileinput.input() then we are read the command args
        else: #No command line args and no file so prompt an error and quit
            print("ERROR: Command line arguments are required\n")
            print("Example Command: python ./SequenceReader.py long.txt short.txt medium.txt")
            print("Example Command: type long.txt | python ./SequenceReader.py")
            quit();

    #Outputs the top 100 sequences in the dictionary to the screen from highest to lowest value
    def Output_Sorted_Dictionary(dict):
        #Sorts the dictionary by value from highest to lowest (key=lambda x:x[1] lets us sort by value, reverse=true lets us sort in descending order)
        sorted_dict = sorted(dict.items(),key=lambda x:x[1], reverse=True)
        top_hundred = 0
        for item in sorted_dict: #Go through each item in the dictionary until we are done or hit 100 items
            if top_hundred == 100: #If we hit 100 items we break because we have output all the needed items
                break;
            top_hundred +=1
            print(f'{top_hundred} {item[0]} - {item[1]}') #Outputs the number we are at in the sorted dictionary and the item associated with the position
        
        return sorted_dict #return the sorted dictionary to see if it is needed for a test

    #Removes unneeded puncutation, turns the text to lower case, and gets rid of white spaces in a line
    def Fluff_Remover(text):
        text = text.lower() #Make all text lower case
        words = text.split() #Split each word by white space and insert them into a list
        words = [word.strip('.,:;"+=@#$%^&*\|!?()[]<>{}-') for word in words] #For each word in words get rid of all punctuation
        
        #In special cases empty strings can get into the words list so we need to remove them or else they will count as a word in a sequence
        #Noted special cases include 'word -- word' (the "--" would be considered a word when it was split and then made an empty string when punctuation was removed)
        empty_string_remover = 0        
        while empty_string_remover != words.count(''): #While the words list has more than 0 white spaces remove the white spaces
            words.remove('') #removes the next white space in the words list
        
        return words #Return the words with no fluff in them to be parsed through for sequences

    #Checks to see if the file given is a text file
    #Could not put file_name == '<stdin>' check in here because the error 'The process tried to write to a nonexistent pipe' would appear
    def File_Extension_Check(file_name):
        extension = os.path.splitext(file_name)[1] #Gets the file extension from the file
        if extension != ".txt": #If the file is not a text file output error and what file caused it
            print("ERROR: All files must be text files!")
            print(f"File Error: {file_name}")
            return True
