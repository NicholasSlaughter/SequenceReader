# SequenceReader
Reads a sequence from a text and outputs the 100 most frequent sequences in the text.

Author: Nicholas Slaughter
Date Created: 6/28/2021
Date Last Modified: 6/30/2021
Purpose: Coding Challenge For New Relic
Description: This program reads through a text file or files and parses through them looking for every sequence of 3 words.
The program checks to see how frequent each time a similar sequence of 3 words comes up and then sorts them into a list from
most frequent to least frequent. Either the total amount of sequences in the text file will be outputed in descending order or
the top 100 sequences will be outputed to the screen (whichever is smaller).

Text files (.txt) are the only file type that are accepted. All other file types given will have an error message printed to the
screen, the user will be told what the bad file was, and the program will be stopped. If a user uses a file that does not exist
an error message will be printed and let the user know what file it was that it could not find.

The program takes in input from the command line either through arguments or piping a file in through stdin.
Examples of running the program from the command line:
command line args: python ./SequenceReader.py long.txt short.txt medium.txt
Piping in files: type long.txt | python ./SequenceReader.py

Note: cat long.txt | python ./SequenceReader.py short.txt will only run the short.txt
Note: if on windows os use 'type' instead of 'cat'
Note: The medium.txt file reads "The Tell-Tale Heart" by Edgar Allen Poe
Note: The long.txt file reads "The Hobbit" by JRR Tolkien
Note: Medium.txt and long.txt were only used for testing purposes to make sure the code worked
Note: A docker file has been added for this program for it to be contanerized
Note: You can pull and run my docker image from the following: nicholasslaughter/sequence_reader:v3

Tests:
There are 18 tests for this program. These tests read the files too see if their output is expected.
All Tests pass and the over all duration to complete these tests is about 2 seconds (Some tests handle multiple large files)

How To Run:
To run the program please follow the following steps:
1. Open the command line prompt window
2. Change your working directory to the second SequenceReader directory
    a. Example: cd C:\SequenceReader\SequenceReader
3. Now execute commands that follow similar patterns:
    a. python ./SequenceReader.py file1.txt file2.txt file3.txt ...
    b. cat file1.txt | python ./SequenceReader.py
        a. If user is on windows os use 'type' instead of 'cat'
4. Some files are given in the solution folder that can be used:
    a. short.txt
    b. medium.txt
    c. long.txt
    b. weirdlines.txt
    e. bad.txt
    f. unicodetest.txt (won't work)

How To Create and Run Docker Image:
1. Open the command line prompt window
2. Change your working directory to the second SequenceReader directory
    a. Example: cd C:\SequenceReader\SequenceReader
3. Execute the following command: docker build -t tag_name:v1
    a. tag_name can be whatever you want to call the image
4. Execute the following command to run the docker container:
    a. docker run -it --rm tag_name:v1 file1.txt file2.txt file3.txt
    
How To Run My Docker Image:
1. Open the command line prompt window
2. Change your working directory to the second SequenceReader directory
    a. Example: cd C:\SequenceReader\SequenceReader
3. Execute the following command to run the docker container:
    a. docker run -it --rm nicholasslaughter/sequence_reader:v3 file1.txt file2.txt file3.txt
    
What I would have done next time if given more time:
1. I would have looked more into using argparser instead of using fileinput
    a. Every time I had to look something up about command line arguments all of the documentation was on argpars and not fileinput
    b. fileinput has some limitations that made coding more challenging
2. Have the program handle unicode characters
    a. I have never dealt with unicode characters before and is something I would like to be able to handle in the future
    b. When looking into how to get the unicode to come out right, it seemed like it would take further research. this would have likely exceeded the duration of this project.
    c. I did attempt to handle unicode but it proved to be more difficult with the little knowledge I had for the time I had left in the coding challenge
3. Get rid of the large code block of conditional statements for if the current line has 1 or 2 words in it
    a. The code makes the Parse_File function harder to read
    b. To do this I would have had to return both a flag of whether or not to continue to the next line and a dictionary with the new values that the current working dictionary should have
    c. I did use the code 'sequence_dict, continu_flag = new_line_check(new_line_sequence,words,sequence_dict)' and used 'return seq_dict, continu_flage' to return from the function
        a. Python does allow for you to return 2 or more arguments but when I ran this, bugs would occur where the dictionary or the continue flage would not be filled
4. Add ability to either run all of the files as one large file or run all the files seperate and see what is the most common sequence for all of the files individually
5. See if there is a way to run a unittest that simulates the command 'cat file1.txt | python ./SequenceReader.py'

Assumptions Made:
1. Program was to run all files passed in as 1 large file and see what the most common sequence of words was
2. Sequences that came up the same amount of time as other sequences would not hold the same position instead one would be positioned lower than the other in the top 100
3. the character '-' should be stripped out of all words because of some instances where 'word -- word' would come up and '--' should not be counted as a word in a sequence
4. Only text files (.txt) are allowed

Bugs:
1. If file has unicode in it the program will not be able to read it
2. Not sure if this is a bug or if it is part of the operating system but if you run the following code: 'cat long.txt | python ./SequenceReader.py short.txt' only short.txt will be read
3. Any file passed as stdin will not have its file extension read because the file name for stdin input is '<stdin>'
    a. From what I read it seems not possible to get the actual file name when passing an argument through stdin
