"""
once make word guess is called in the word class it should allow for input at the moment so that the user can enter what was green and what was yellow and grey and then from there it should call possible words and do the following:
 1. if its green make sure you only have words that have that letter at that index
 2. if its yellow make sure that you get rid of any words with that letter at that index and make sure you make sure that the word must include that letter at some point
3. if its grey just call get rid of letter and add it to the list of letters that cant be used
have to make sure that once a letter is confirmed it can never be changed from that position
"""
class possibleWords:
  def __init__(self,possibleWords):
    self.possibleWords = possibleWords

  def __str__(self):
    wordsListedOut = ""
    for word in self.possibleWords:
      wordsListedOut += f"{word}\n"
    return wordsListedOut
  
  def getRidOfLetter(self,letter):
    wordSetNew = set()
    for word in possibleWords:
      if letter not in word:
        wordSetNew.add(word)
    self.possibleWords = wordSetNew
    
  def mustIncludeLetter(self,letter):
    wordSetNew = set()
    for word in possibleWords:
      if letter in word:
        wordSetNew.add(word)
    self.possibleWords = wordSetNew
    
  def getRidOfLetterAtIndex(self,letter,index):
    wordSetNew = set()
    for word in possibleWords:
      if word[index] != letter:
        wordSetNew.add(word)
    self.possibleWords = wordSetNew
    
  def wordMustIncludeLetterAtIndex(self,letter,index):
    wordSetNew = set()
    for word in possibleWords:
      if word[index] == letter:
        wordSetNew.add(word)
    self.possibleWords = wordSetNew
    
class word:
  def __init__(self,firstWord,possibleWords):
    self.firstWord = firstWord
    self.possibleWords = possibleWords
    self.finalWord = "00000"
    self.badLetters = []
    self.goodLetters = []
  def solvePuzzle(self):
    pass
  def makeWordGuess(self,word):
    pass
  
def run():
  possibleWordsReader = set()
  with open("fiveCharacterWords.txt","r") as reader:
    for line in reader:
      possibleWordsReader.add(line.strip("\n"))
  possibleWordsObj = possibleWords(possibleWordsReader)
  print(possibleWordsObj)
  
if __name__ == "__main__":
  run()