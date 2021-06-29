import unittest
import fileinput
from SequenceReader import main

class Test_SequenceReaderTests(unittest.TestCase):

    def test_ReadShortStoryText_WithValidShortStoryText_ReturnsExpectedDictionary(self):
        try:
            expected_short_dict = [("i am nick", 3), ("nick i am", 2), ("am nick i", 1), ("am nick my", 1),
                                  ("nick my name", 1), ("my name is", 1), ("name is nick", 1), ("is nick i", 1)]
            f= 'short.txt'
            result = main(f)
            self.assertTrue(result==expected_short_dict)
        except:
            self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
