import os

def main():
    letters = [
        file.removesuffix('.svg')
        for file in os.listdir('font/letters')
        if file.endswith('.svg')
    ]
    print(letters)

if __name__=='__main__':
   main() 
