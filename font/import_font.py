import os
import unittest

class Glyph:
    def __init__(self, name):
        self.name = name 
        self.svg_file = f'font/glyphs/{name}.svg'

class FontMaker:
    def __init__(self):
        self.glyphs = [
            Glyph(file.removesuffix('.svg'))
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
        self.assertEqual(len(unique_names), len(glyphs))

    def test_we_have_a_glyph_named_tcha(self):
        found = [glyph for glyph in FontMaker().glyphs if glyph.name == 'tcha']
        self.assertEqual(len(found), 1)

    def test_each_glyph_has_an_openable_svg_file(self):
        for glyph in FontMaker().glyphs:
            with open(glyph.svg_file) as f:
                pass

if __name__=='__main__':
    unittest.main()
    main()
