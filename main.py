"""
wordConfirmedChars = [[],[],[],[],[]]
wordDontIncludeChars = [[],[],[],[],[]]
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

      
def run():
  possibleWordsReader = set()
  with open("fiveCharacterWords.txt","r") as reader:
    for line in reader:
      possibleWordsReader.add(line.strip("\n"))
  possibleWordsObj = possibleWords(possibleWordsReader)
  print(possibleWordsObj)
  
if __name__ == "__main__":
  run()