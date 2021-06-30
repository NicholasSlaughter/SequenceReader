import unittest
import fileinput
from SequenceReader import main

class Test_SequenceReaderTests(unittest.TestCase):

    def test_ReadShortText_WithValidShortStoryText_ReturnsExpectedDictionary(self):
        try:
            expected_short_dict = [("i am nick", 3), ("nick i am", 2), ("am nick i", 1), ("am nick my", 1),
                                  ("nick my name", 1), ("my name is", 1), ("name is nick", 1), ("is nick i", 1)]
            f= 'short.txt'
            result = main(f)
            self.assertTrue(result==expected_short_dict)
        except:
            self.fail("dictionary returned does not match the expected")

    def test_ReadWeirdLinesText_WithValidWeirdLinesText_ReturnsExpectedDictionary(self):
        try:
            expected_weird_line_dict = [("i am nick", 1), ("am nick i'm", 1), ("nick i'm cool", 1), ("i'm cool yes", 1),
                                  ("cool yes super", 1), ("yes super cool", 1), ("super cool because", 1), ("cool because i'm", 1), ("because i'm nick", 1)]
            f= 'weirdlines.txt'
            result = main(f)
            self.assertTrue(result==expected_weird_line_dict)
        except:
            self.fail("dictionary returned does not match the expected")

    def test_ReadMediumText_WithValidMediumText_ReturnsExpectedDictionary(self):
        try:
            expected_medium_dict = [("the old man", 8), ("the old man's", 5), ("it was the", 4), ("he had been", 4), ("but the noise", 4)]
            f= 'medium.txt'
            i=0
            check = True

            result = main(f)
            while i < 5:
                if expected_medium_dict[i] != result[i]:
                    check = False
                    break
                i+=1

            self.assertTrue(check)
        except:
            self.fail("dictionary returned does not match the expected")

if __name__ == '__main__':
    unittest.main()
