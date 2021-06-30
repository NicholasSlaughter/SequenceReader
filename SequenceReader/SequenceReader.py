from Helper import Helper
from FileSearch import FileSearch

#Name: Nicholas Slaughter
#Date Created: 6/28/2021
#Date Last Modified: 6/30/2021
#Purpose: Coding Challenge For New Relic
#Description: This program reads through a text file or files and parses through them looking for every sequence of 3 words.
#The program checks to see how frequent each time a similar sequence of 3 words comes up and then sorts them into a list from
#most frequent to least frequent. Either the total amount of sequences in the text file will be outputed in descending order or
#the top 100 sequences will be outputed to the screen (whichever is smaller).
#
#The program takes in input from the command line either through arguments or piping a file in.
#Examples of running the program from the command line:
#command line args: python ./SequenceReader.py long.txt short.txt medium.txt
#Piping in files: type long.txt | python ./SequenceReader.py
#Note: type long.txt | python ./SequenceReader.py short.txt will only run the short.txt
#Note: type is windows version of cat from linux

def main(files=None):
    #Parses the filestream for the frequency that sequences of 3 words appear
    #Those sequences are then put that into a dictionary which is then sorted by most frequent to least frequent sequence
    sorted_dict = FileSearch.Parse_File(files) #Returns a sorted dictionary of most frequent to least frequent sequence

    #If test files were used return the sorted dictionary to see if its test passes
    if files:
        return sorted_dict

if __name__ == "__main__":
    main()