import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
        self.assertListEqual( ['yeah'], unique(['yeah']) )
        self.assertListEqual( ['compro'], unique(['compro']) )
        self.assertListEqual( ['2019'], unique(['2019']) )
    
    def test_empty_item_list(self):
        self.assertListEqual( [], unique([]) )

    def test_one_item_many_time_list(self):
        self.assertListEqual( ['h'], unique(['h','h','h']) )
        self.assertListEqual( ['3'], unique(['3','3','3','3']) )
        self.assertListEqual( ['hiii'], unique(['hiii','hiii','hiii']) )
        self.assertListEqual( ['eiei'], unique(['eiei','eiei']) )
 
    def test_two_item_many_time_list(self):
        self.assertListEqual( ['a','b'], unique(['a','b','b','a']) )
        self.assertListEqual( ['3','4'], unique(['3','3','3','4']) )
        self.assertListEqual( ['zi','za'], unique(['zi','zi','zi','zi','za','za']) )

    def test_list_in_list(self):
        self.assertEqual([0,2,1,[10,20],[11,25,30]], unique([0,2,1,[10,20],[11,25,30]]))

       
    

if __name__ == '__main__':
    unittest.main()