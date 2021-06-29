import fileinput
import sys
from DictionaryHelper import DictionaryHelper

#command line args: python ./SequenceReader.py long.txt short.txt medium.txt
#Piping in files: type long.txt | python ./SequenceReader.py
#type is windows version of cat from linux

def main(files=None):

    sequence_dict = {}
    unfinished_sequence = []
    sequence_of_second_last_line = ''
    sequence_of_last_line = ''
    f = ''

    if files: #No args and file descriptor is open means it is a test so run test file
        f = fileinput.input(files=(files))
    elif len(sys.argv) > 1 or not sys.stdin.isatty(): #There are commands from the command line so lets run them
        f= fileinput.input()
    else: #No command line args and no file so throw error
        print("ERROR: Command line arguments are required\n")
        print("Example Command: python ./SequenceReader.py long.txt short.txt medium.txt")
        print("Example Command: type long.txt | python ./SequenceReader.py")
        quit();

    for line in f:
        if line == '\n':
            continue
        text = line.lower()
        words = text.split()
        words = [word.strip('.,:;"+=@#$%^&*\|!?()[]<>{}-') for word in words]

        space_remover = 0

        while space_remover != words.count(''):
            words.remove('')

        sequence = ''         

        if sequence_of_last_line:
            if len(words) < 2: #1 word on the line
                sequence = sequence_of_last_line[1] + ' ' + sequence_of_last_line[2] + ' ' + words[0]
                sequence_dict[sequence] = DictionaryHelper.Add_To_Dictionary(sequence,sequence_dict)
                sequence_of_last_line = [(sequence_of_last_line[2]), (sequence_of_last_line[2]), (words[0])] #fill the sequence back up to work for the next line
                continue

            #TODO sometimes the new line and the last line won't have 3 characters on it so you have to go to the next one
            sequences = [sequence_of_last_line[1] + ' ' + sequence_of_last_line[2] + ' ' + words[0],
                        sequence_of_last_line[2] + ' ' + words[0] + ' ' + words[1]]
            for sequence in sequences:
                sequence_dict[sequence] = DictionaryHelper.Add_To_Dictionary(sequence,sequence_dict)
        if len(words) == 2:
            sequence_of_last_line = [(sequence_of_last_line[2]), (words[0]), (words[1])] #fill the sequence back up to work for the next line
            continue

        i=0
        sequence = ''
        while i+2 < len(words):
            sequence = words[i] + ' ' + words[i+1] + ' ' + words[i+2]            
            sequence_dict[sequence] = DictionaryHelper.Add_To_Dictionary(sequence,sequence_dict)
            i+=1

        sequence_of_last_line = sequence.split()

    sorted_dict = sorted(sequence_dict.items(),key=lambda x:x[1], reverse=True)
    top_hundred = 0
    for item in sorted_dict:
        if top_hundred == 100:
            break;
        top_hundred +=1
        print(f'{top_hundred} {item[0]} - {item[1]}')

    if files:
        return sorted_dict

if __name__ == "__main__":
    main()