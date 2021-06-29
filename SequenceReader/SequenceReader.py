import fileinput
import sys
from DictionaryHelper import DictionaryHelper

def main(file=None):

    sequence_dict = {}
    unfinished_sequence = []
    sequence_of_second_last_line = ''
    sequence_of_last_line = ''

    for line in fileinput.input():
        if line == '\n':
            continue
        text = line.lower()
        words = text.split()
        words = [word.strip('.,:;"+=@#$%^&*\|!?()[]<>{}-') for word in words]
        sequence = ''         

        if sequence_of_last_line:
            print(sequence_of_last_line[1] + ' ' + sequence_of_last_line[2] + ' ' + words[0])

            if len(words) < 2: #1 word on the line
                sequence = sequence_of_last_line[1] + ' ' + sequence_of_last_line[2] + ' ' + words[0]
                sequence_dict[sequence] = DictionaryHelper.Add_To_Dictionary(sequence,sequence_dict)
                sequence_of_last_line = [(sequence_of_last_line[2]), (sequence_of_last_line[2]), (words[0])] #fill the sequence back up to work for the next line
                continue

            print(sequence_of_last_line[2] + ' ' + words[0] + ' ' + words[1])

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

    if file:
        return sorted_dict

if __name__ == "__main__":
    main()