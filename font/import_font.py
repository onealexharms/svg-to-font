import os

CONSONANTS = [ 'B', 'D', 'DJ', 'G', 'K', 'L', 'M', 'T', 'TCH', 'Z' ]

def main():
    for consonant in CONSONANTS:
        files = [
            file
            for file in os.listdir('font/' + consonant)
            if file.endswith('.svg')
        ]
        print(files)

if __name__=='__main__':
   main() 
