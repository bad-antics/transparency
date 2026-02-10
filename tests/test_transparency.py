import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from transparency.core import TransparencyEngine

class TestTransparency(unittest.TestCase):
    def test_concept(self):
        t=TransparencyEngine()
        r=t.explore_concept("transparency")
        self.assertIn("paradox",r)
    def test_index_obscene(self):
        t=TransparencyEngine()
        r=t.transparency_index({"surveillance":True,"data_collection":True,"social_scoring":True,"no_privacy":True})
        self.assertEqual(r["state"],"OBSCENE")
    def test_index_opaque(self):
        t=TransparencyEngine()
        r=t.transparency_index({})
        self.assertEqual(r["state"],"OPAQUE")

if __name__=="__main__": unittest.main()
