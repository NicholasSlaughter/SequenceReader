import fileinput
import sys

def main(file=None):

    sequence_dict = {}
    unfinished_sequence = []
    last_sequence_of_line = ''

    for line in fileinput.input():
        if line == '\n':
            continue
        text = line.lower()
        words = text.split()
        words = [word.strip('.,:;"+=@#$%^&*\|!?()[]<>{}') for word in words]

        if last_sequence_of_line:
            print(last_sequence_of_line[1] + ' ' + last_sequence_of_line[2] + ' ' + words[0])
            print(last_sequence_of_line[2] + ' ' + words[0] + ' ' + words[1])

            #TODO sometimes the new line and the last line won't have 3 characters on it so you have to go to the next one
            sequences = [last_sequence_of_line[1] + ' ' + last_sequence_of_line[2] + ' ' + words[0],
                        last_sequence_of_line[2] + ' ' + words[0] + ' ' + words[1]]
            for seq in sequences:
                if seq not in sequence_dict:
                    sequence_dict[seq]=0
                sequence_dict[seq]+=1

        i=0
        sequence = ''
        while i+2 < len(words):
            sequence = words[i] + ' ' + words[i+1] + ' ' + words[i+2]
            if sequence not in sequence_dict:
                sequence_dict[sequence]=0
            sequence_dict[sequence]+=1
            i+=1

        last_sequence_of_line = sequence.split()

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