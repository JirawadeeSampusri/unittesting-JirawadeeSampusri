import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
    
    def test_empty_item_list(self):
        self.assertListEqual( [], unique([]) )

    def test_one_item_many_time_list(self):
        self.assertListEqual( ['h'], unique(['h','h','h']) )
 
    def test_two_item_many_time_list(self):
        self.assertListEqual( ['a','b'], unique(['a','b','b','a']) )
    
    def test_error_list(self):
        self.assertListEqual( ['a'], unique(['a','b','b','a']) )


 
if __name__ == '__main__':
    unittest.main()