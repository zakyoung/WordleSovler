"""
once make word guess is called in the word class it should allow for input at the moment so that the user can enter what was green and what was yellow and grey and then from there it should call possible words and do the following:
 1. if its green make sure you only have words that have that letter at that index
 2. if its yellow make sure that you get rid of any words with that letter at that index and make sure you make sure that the word must include that letter at some point
3. if its grey just call get rid of letter and add it to the list of letters that cant be used
have to make sure that once a letter is confirmed it can never be changed from that position
"""
class possibleWords:
  def __init__(self,possibleWordsList):
    self.possibleWordsList = possibleWordsList

  def __str__(self):
    wordsListedOut = ""
    for word in self.possibleWordsList:
      wordsListedOut += f"{word}\n"
    return wordsListedOut
  
  def getRidOfLetter(self,letter):
    wordListNew = []
    for word in self.possibleWordsList:
      if letter not in word:
        wordListNew.append(word)
    self.possibleWordsList = wordListNew
    
  def mustIncludeLetter(self,letter):
    wordListNew = []
    for word in self.possibleWordsList:
      if letter in word:
        wordListNew.append(word)
    self.possibleWordsList = wordListNew
    
  def getRidOfLetterAtIndex(self, letter,index):
    wordListNew = []
    for word in self.possibleWordsList:
      if word[index] != letter:
        wordListNew.append(word)
    self.possibleWordsList = wordListNew
    
  def mustIncludeLetterAtIndex(self, letter,index):
    wordListNew = []
    for word in self.possibleWordsList:
      if word[index] == letter:
        wordListNew.append(word)
    self.possibleWordsList = wordListNew
    
class wordGuesser:
  def __init__(self,firstWord,possibleWordsObj):
    self.guess = firstWord
    self.possibleWordsObj = possibleWordsObj
    self.finalWord = [0,0,0,0,0]
  def solvePuzzle(self):
    guessCount = 0
    yellows = []
    while guessCount <= 6 and 0 in self.finalWord:
      print(f"Guessed Word: {self.guess}")
      isRealWord = input("Is this a word you can guess type y for yes and n for no: ")
      while isRealWord == "n":
        self.possibleWordsObj.possibleWordsList.remove(self.guess)
        self.guess = self.possibleWordsObj.possibleWordsList[0]
        print(f"Guessed Word: {self.guess}")
        isRealWord = input("Is this a word you can guess type y for yes and n for no: ")
      print("Enter g for green, y for yellow, and b for black")
      for index,letter in enumerate(self.guess):
        characteristic = input(f"{letter}: ")
        if characteristic == "g":
          self.possibleWordsObj.mustIncludeLetterAtIndex(letter, index)
          self.finalWord[index] = letter
        elif characteristic == "y":
          yellows.append(letter)
          self.possibleWordsObj.getRidOfLetterAtIndex(letter, index)
          self.possibleWordsObj.mustIncludeLetter(letter)
        else:
          if letter in yellows:
            self.possibleWordsObj.getRidOfLetterAtIndex(letter, index)
          else:
            self.possibleWordsObj.getRidOfLetter(letter)
      guessCount += 1
      self.guess = self.possibleWordsObj.possibleWordsList[0]
    try:
      return "".join(self.finalWord)
    except:
      return "We could not succesfully determine the word in six tries"
def run():
  possibleWordsReader = []
  with open("fiveCharacterWords.txt","r") as reader:
    for line in reader:
      possibleWordsReader.append(line.strip("\n"))
    possibleWordsObj = possibleWords(possibleWordsReader)
    guesser = wordGuesser("adieu", possibleWordsObj)
    print(f"The answer to the wordle is: {guesser.solvePuzzle()}")
if __name__ == "__main__":
  run()