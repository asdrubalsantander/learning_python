#Ex15

def reversedPhrase(phrase):
    return ' '.join(phrase.split()[::-1])

def main():
  phrase = input("Give me a phrase to reverse it: ")
  print( phrase + ' <-> ' + reversedPhrase(phrase))

if __name__ == "__main__":
    main()