import csv
acceptedWords = []
with open("wordlist.txt", 'r') as words:
    for word in words:
        if(len(word) > 4):
            acceptedWords.append(word.strip())
            print(word)

with open("wordlist.csv", "w", newline='') as file:
    writer = csv.writer(file)
    for word in acceptedWords:
        writer.writerow([word])
          
