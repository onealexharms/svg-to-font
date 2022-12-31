import os

def main():
    glyphs = [
        file.removesuffix('.svg')
        for file in os.listdir('font/glyphs')
        if file.endswith('.svg')
    ]
    print(glyphs)

if __name__=='__main__':
   main()
