from Helper import Helper
import sys

class FileSearch(object):
    
    #Parses through a file(s) line by line to get every sequence of 3 words in the file(s)
    #A dictionary is updated every sequence either by adding the sequence to the list if it's new or incrementing its value by 1 if it is not new
    def Parse_File(files):
        #Variables
        sequence_dict = {}
        new_line_sequence = ''
        file_stream=''
        first_file=''

        #Checks to see if the program should except input from the command line or from test files
        file_stream = Helper.Input_Check(files) #Returns filestream of the needed files

        for line in file_stream:
            #If the current line is a new line break then immediately continue to the next line in the file stream
            if line == '\n':
                continue

            #If the current file is read from stdin we do not want to check the file extension because it will
            #see that it is not a txt file and throw an error
            if file_stream.filename() != '<stdin>':
                if file_stream.isfirstline():
                    if not first_file and first_file != 'done': #Grab the first file so we don't run first line checks if there is 1 or 2 words on a line in following files
                        first_file = file_stream.filename()
                    if Helper.File_Extension_Check(file_stream.filename()):
                        return 0

            #If we have a file get piped in and the first line hasn't already been read
            #then we need to set the first first file var to <stdin>
            if file_stream.filename() == '<stdin>' and first_file != 'done':
                first_file = '<stdin>'
                

            words = Helper.Fluff_Remover(line) #Remove punctuation, white spaces, and make all words lower case

            #If the last line had a sequence then we want to snake that sequence down to the next line
            if new_line_sequence:
                
                #If the current line we are on has 1 word then we have to add that word to a sequence and move on to the next line
                if len(words) < 2:
                    #The very first line had only 1 word so snake to next line
                    if len(new_line_sequence) == 1:
                        #update the new line sequence to work for the next line
                        new_line_sequence = [(new_line_sequence[0]), (words[0])]
                        continue #Only had 1 word in the line so immediatly continue to the next line

                    #The first second and third line had only one word on them so put the complete sequence into the dictionary and move to the next line
                    if len(new_line_sequence) == 2:
                        sequence = new_line_sequence[0] + ' ' + new_line_sequence[1] + ' ' + words[0]
                        
                        #Add the sequence to the database and update its value depending on if it is a new sequence or not
                        sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict)

                        #update the new line sequence to work for the next line
                        new_line_sequence = [(new_line_sequence[0]), (new_line_sequence[1]), (words[0])]
                        continue #Only had 1 word in the line so immediatly continue to the next line

                    if len(new_line_sequence) > 2:
                        #Make a sequence with the last 2 words from the previous line and the 1 word from the current line
                        sequence = new_line_sequence[1] + ' ' + new_line_sequence[2] + ' ' + words[0]

                        #Add the sequence to the database and update its value depending on if it is a new sequence or not
                        sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict)

                        #update the new line sequence to work for the next line
                        new_line_sequence = [(new_line_sequence[1]), (new_line_sequence[2]), (words[0])]
                        continue #Only had 1 word in the line so immediatly continue to the next line

                #The very first line had only 1 word so snake to next line
                if len(new_line_sequence) == 1:
                    sequence = new_line_sequence[0] + ' ' + words[0] + ' ' + words[1]
                    sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict)

                    #If the second line has 2 words then update the new line sequence and move on to the next line
                    if len(words) == 2:
                        new_line_sequence = [(new_line_sequence[0]), (words[0]), (words[1])]
                        continue

                #If the first line only had 1 word and the second line only had one word then fill
                if len(new_line_sequence) == 2:
                    sequences = [new_line_sequence[0] + ' ' + new_line_sequence[1] + ' ' + words[0],
                                new_line_sequence[1] + ' ' + words[0] + ' ' + words[1]]

                    #For each sequence in sequences add the sequence to the dictionary and update its value
                    for sequence in sequences:
                        sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict)

                if len(new_line_sequence) > 2:
                    #If the current line has 2 or more word then add that to a sequence including words from the previous line
                    sequences = [new_line_sequence[1] + ' ' + new_line_sequence[2] + ' ' + words[0],
                                new_line_sequence[2] + ' ' + words[0] + ' ' + words[1]]

                    #For each sequence in sequences add the sequence to the dictionary and update its value
                    for sequence in sequences:
                        sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict)
            
            #If we are on the first line of the first file and there is only 1 or 2 words then update the new line sequence and move to the next line
            if file_stream.isfirstline() and first_file == file_stream.filename():
                first_file='done'
                if len(words) ==1:
                    new_line_sequence = [(words[0])]
                    continue
                if len(words) ==2:
                    new_line_sequence = [(words[0]), (words[1])]
                    continue            

            #If there is only 2 words on the current line then we have already added the needed sequences to the dictionary so we continue to the next line
            if len(words) == 2:
                new_line_sequence = [(new_line_sequence[2]), (words[0]), (words[1])] #update the new line sequence to work for the next line
                continue

            #Go through the line and add each sequence of 3 words to the dictionary
            #If the sequence is already in the dictionary its value will be updated if it is a new sequence it will be added
            i=0
            sequence=''
            while i+2 < len(words): #Loop through the words in the line (We access i+2 inside the loop so must check if we aren't over the length)
                sequence = words[i] + ' ' + words[i+1] + ' ' + words[i+2] #Add the next 3 words to a sequence            
                sequence_dict[sequence] = Helper.Add_To_Dictionary(sequence,sequence_dict) #Check to see if the sequence is new and update its value
                i+=1 #increment the iterator for the next phase of the loop

            new_line_sequence = sequence.split() #split the last sequence into a list to be used for snaking the sequences into the next line

        #If the dictionary is empty then the file did not contain at least 3 words
        if not sequence_dict:
            print("ERROR: Text File Must Include At Least 3 Words")
            return 0

        return Helper.Output_Sorted_Dictionary(sequence_dict) #Sort the dictionary and return to main

