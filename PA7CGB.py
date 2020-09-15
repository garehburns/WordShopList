import re

# Read and return words from file as array
def getWordsFromFile() :
        words = []

        # Open File to read
        with open("Story.txt", 'r') as iFile:
                lines = [word.upper() for line in iFile for word in line.split()]
        
        # Loop through lines in file
        for line in lines:
                line = line.split()
                line.sort(reverse = False)
                line.sort(key = lambda x:x.upper())

                # Loop through words in line
                for word in line:
                        word = word.strip("(- : ! . , \"")
                        words.append(word)

        
        iFile.close() # Close File
        return words  # Return words from file


def main() :
        usedWords = []

        # Open file for outputting
        oFile = open("WorkShopList.txt", 'w')
        oFile.write("Word\t\t\t" + "Number of Occurences\n")
        oFile.write("-------\t\t\t" + "------------------------------\n")

        wordList = getWordsFromFile()
        wordList = sorted(wordList)
        
        for word in wordList :
                if usedWords.count(word) > 0 :  # If the word is a usedWord then dont procede, continue to top of loop
                        continue
                else :  # Else append it to used words
                        usedWords.append(word)

                # Output the word and the count
                oFile.write(word + "\t\t\t\t" + str(wordList.count(word)))
                oFile.write('\n')

        oFile.close()

# Start program
main()
