# WordleSovler
This program has the intended purpose of solving the popular puzzle game wordle. Right now it is implemented using input from the user but eventually we plan
to hook it directly up to the wordle website. The program works by starting with every 5 letter word in the enlgish dictionary and then from there narrowing
the possible words down using one of the following cases:
1. If the letter is not in the word aka the letter appears black we remove every word in the dictionary that has that word in it
2. If the letter is in the word but not in the correct positon we remove every word with the letter at that index and then we only keep words that have that letter somewhere in the word
3. If the letter is in the word in the correct position we narrow the set down to words that have that letter in that position
