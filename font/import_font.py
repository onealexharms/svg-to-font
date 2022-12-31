import os
import unittest

class Glyph:
    def __init__(self, name):
        self.name = name 

class FontMaker:
    def __init__(self):
        self.glyphs = [
            Glyph(file)
            for file in os.listdir('font/glyphs')
            if file.endswith('.svg')
        ]

class Tests(unittest.TestCase):
    def test_there_are_80_glyphs(self):
        self.assertEqual(len(FontMaker().glyphs), 80)

    def test_every_glyph_has_a_unique_name(self):
        glyphs = FontMaker().glyphs
        for glyph in glyphs:
            self.assertIsInstance(glyph.name, str)
        unique_names = set([glyph.name for glyph in glyphs]) 
        self.assertEquals(len(unique_names), len(glyphs))

if __name__=='__main__':
    unittest.main()
    main()
