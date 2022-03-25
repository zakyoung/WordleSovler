possibleWordsReader = []
with open("fiveCharacterWords.txt","r") as reader:
  for line in reader:
    possibleWordsReader.append(line.strip("\n"))
sortedWords = sorted(possibleWordsReader,key = lambda x:len(set(list(x))), reverse = True)
with open("specialOrdering.txt","w") as writer:
  for word in sortedWords:
    writer.write(f"{word}\n")
  
  