import unittest
import fileinput

class Test_SequenceReaderTests(unittest.TestCase):
    expected_short_dict = {}

    def test_ReadShortStoryText_WithValidShortStoryText_ReturnsExpectedDictionary(self):
        try:
            f= fileinput.input(files=('short.txt'))
            result = main(f)
            self.assertTrue(result==expected_short_dict)
        except:
            self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
