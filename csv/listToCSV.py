import csv
acceptedWords = []
"""
This file reads the wordlist.txt of words and those of length 5 or higher
get added to a CSV of words to be used for the mini-games
"""
with open("wordlist.txt", 'r') as words:
    for word in words:
        if(len(word) > 4):
            acceptedWords.append(word.strip())
            print(word)

with open("wordlist.csv", "w", newline='') as file:
    writer = csv.writer(file)
    for word in acceptedWords:
        writer.writerow([word])
          
