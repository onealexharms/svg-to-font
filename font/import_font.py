import os
import unittest

class FontMaker:
    def __init__(self):
        self.glyphs = [
            file.removesuffix('.svg')
            for file in os.listdir('font/glyphs')
            if file.endswith('.svg')
        ]

class TheTests(unittest.TestCase):
    def test_there_are_80_glyphs(self):
        self.assertEqual(len(FontMaker().glyphs), 80)

if __name__=='__main__':
    unittest.main()
    main()
