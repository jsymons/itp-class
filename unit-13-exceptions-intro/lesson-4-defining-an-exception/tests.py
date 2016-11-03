import unittest

class TestExceptions(unittest.TestCase):
    
    def test_custom_string_exception(self):

        def string_length(a_string):
            if len(string) > 7:
                raise StringTooLongException
            else:
                pass
        
        self.assertRaises(StringTooLongException, string_length, '001100010010011110100001101101110011')